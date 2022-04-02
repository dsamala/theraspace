from django import forms
from .models import Patient, Clinician
from .models import GENDER_CHOICES

class CreatePatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'gender', 'address', 'zip', 'diagnosis', 'clinician']
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.CharField()
    address = forms.CharField()
    zip = forms.IntegerField()
    diagnosis = forms.CharField()
    clinician = forms.ModelMultipleChoiceField(queryset=Clinician.objects.all(), widget=forms.CheckboxSelectMultiple)



class UpdatePatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'gender', 'address', 'zip', 'diagnosis', 'clinician']
    
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField()
    gender = forms.CharField()
    address = forms.CharField()
    zip = forms.IntegerField()
    diagnosis = forms.CharField()
    clinician = forms.ModelMultipleChoiceField(queryset=Clinician.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
