from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Patient, Clinician
from django.contrib.auth.models import User
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
                    print('The account does not exist or has been disabled.')
                    return HttpResponseRedirect('/login')
            else:
                print('The username and/or password is incorrect.')
                return HttpResponseRedirect('/login')
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
            return HttpResponseRedirect('/login')
        else:
            HttpResponse('<h1>Please Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

class PatientList(TemplateView):
    template_name = 'patient_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = Patient.objects.all()
        return context

class Patient_New(CreateView):
    model = Patient
    fields = ['firstname', 'lastname', 'age', 'gender', 'zip', 'diagnosis', 'clinician']
    template_name = "patient_new.html"
    success_url = '/patients'

class PatientDetail(DetailView):
    model = Patient
    template_name = 'patient_detail.html'

class PatientUpdate(UpdateView):
    model = Patient
    fields = ['firstname', 'lastname', 'age', 'gender', 'zip', 'diagnosis', 'clinician']
    template_name = 'patient_update.html'
    def get_success_url(self):
        return reverse('patient_detail', kwargs={'pk': self.object.pk})

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'patient_delete_confirm.html'
    success_url = '/patients'
