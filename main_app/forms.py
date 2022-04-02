from django import forms
from .models import Patient, Clinician

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
    clinician = forms.ModelMultipleChoiceField(queryset=Clinician.objects.all(), widget=forms.CheckboxSelectMultiple)
