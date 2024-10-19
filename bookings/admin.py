from django.contrib import admin

# Register your models here.
from .models import Appointment, MedicalNote
# Incluyo los modelos de mis tablas en el panel de administración 
admin.site.register(Appointment)
admin.site.register(MedicalNote)
