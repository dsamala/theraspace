from django import forms
from .models import Patient, Clinician
from .models import GENDER_CHOICES
from django.core.validators import MaxValueValidator, MinValueValidator

class CreatePatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'gender', 'address', 'zip', 'diagnosis', 'clinician']
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1, max_value=100, validators=[MaxValueValidator(100), MinValueValidator(1)])
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField()
    zip = forms.IntegerField()
    diagnosis = forms.CharField()
    clinician = forms.ModelMultipleChoiceField(required=False, queryset=Clinician.objects.all(), widget=forms.CheckboxSelectMultiple)



class UpdatePatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'age', 'gender', 'address', 'zip', 'diagnosis', 'clinician']
    
    firstname = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField(min_value=1, max_value=100,validators=[MaxValueValidator(100), MinValueValidator(1)])
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    address = forms.CharField()
    zip = forms.IntegerField()
    diagnosis = forms.CharField()
    clinician = forms.ModelMultipleChoiceField(queryset=Clinician.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
