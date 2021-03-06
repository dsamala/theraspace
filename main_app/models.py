from django.db import models

# Create your models here.

DISCIPLINE_CHOICES = (
    ("PT", "Physical Therapist"),
    ("OT", "Occupational Therapist"),
    ("ST", "Speech Therapist"),
)

GENDER_CHOICES = (
    ("F", "female"),
    ("M", "male")
)

class Clinician(models.Model):
    name = models.CharField(max_length=50)
    discipline = models.CharField(max_length=20, choices=DISCIPLINE_CHOICES)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Patient(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=300)
    zip = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    diagnosis = models.CharField(max_length=150)
    clinician = models.ManyToManyField(Clinician, null=True)

    def __str__(self):
        return self.lastname

    class Meta:
        ordering = ['lastname']
