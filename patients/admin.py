from django.contrib import admin


# Register your models here.
from .models import Patient, Insurance, MedicalRecord
# Incluyo los modelos de mis tablas en el panel de administración 
admin.site.register(Patient)
admin.site.register(Insurance)
admin.site.register(MedicalRecord)