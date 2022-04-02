from django.contrib import admin
from .models import Patient
from .models import Clinician

# Register your models here.
admin.site.register(Clinician)
admin.site.register(Patient)