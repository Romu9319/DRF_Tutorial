from django.contrib import admin

# Register your models here.
from .models import Doctor, Department, DoctorAvailability, MedicalNote
# Incluyo los modelos de mis tablas en el panel de administración 
admin.site.register(Doctor)
admin.site.register(Department)
admin.site.register(DoctorAvailability)
admin.site.register(MedicalNote)