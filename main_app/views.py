from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .forms import CreatePatientForm, UpdatePatientForm
from django.contrib.auth.models import User
from main_app.forms import UpdatePatientForm
from main_app.models import Patient, Clinician
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = Patient.objects.all()
        context["clinicians"] = Clinician.objects.all()
        return context  

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'signup.html', {'form': form})
        else: 
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})        


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class PatientList(TemplateView):
    template_name = 'patient_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        checkpatients = self.request.GET.get("checkpatients")
        if name != None:
            context["patients"] = Patient.objects.filter(Q(lastname__icontains=name) | Q(firstname__icontains=name))
        else:
            context["patients"] = Patient.objects.all()
        if checkpatients:
            context["patients"] = Patient.objects.filter(clinician__isnull=True)
        return context

@method_decorator(login_required, name='dispatch')
class Patient_New(CreateView):
    model = Patient
    form_class = CreatePatientForm
    template_name = "patient_new.html"
    success_url = '/patients'

@method_decorator(login_required, name='dispatch')
class PatientDetail(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

@method_decorator(login_required, name='dispatch')
class PatientUpdate(UpdateView):
    model = Patient
    form_class = UpdatePatientForm
    template_name = 'patient_update.html'
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class PatientDelete(DeleteView):
    model = Patient
    template_name = 'patient_delete_confirm.html'
    success_url = '/patients'

@method_decorator(login_required, name='dispatch')
class ClinicianList(TemplateView):
    template_name = 'clinician_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        checkclinicians = self.request.GET.get("checkclinicians")
        if name != None:
            context["clinicians"] = Clinician.objects.filter(Q(name__icontains=name))
        else:
            context["clinicians"] = Clinician.objects.all()
        if checkclinicians:
            context["clinicians"] = Clinician.objects.filter(patient__isnull=True)
        return context

@method_decorator(login_required, name='dispatch')
class Clinician_New(CreateView):
    model = Clinician
    fields = ['name', 'discipline']
    template_name = 'clinician_new.html'
    success_url = '/clinicians'


def clinician_show(request, clinician_id):
    clinician = Clinician.objects.get(id=clinician_id)
    patients = list(clinician.patient_set.all())
    return render(request, 'clinician_detail.html', {'clinician': clinician, 'patients': patients})        

@method_decorator(login_required, name='dispatch')
class ClinicianUpdate(UpdateView):
    model = Clinician
    fields = ['name', 'discipline']
    template_name = 'clinician_update.html'
    success_url = '/clinicians'


@method_decorator(login_required, name='dispatch')
class ClinicianDelete(DeleteView):
    model = Clinician
    template_name = 'clinician_delete_confirm.html'
    success_url = '/clinicians'
    
