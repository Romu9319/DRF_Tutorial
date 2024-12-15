from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor
# Create your tests here.
class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name = 'Jose',
            last_name = 'Avila',
            date_of_birth = '1995-11-07',
            contact_number = '123456789',
            email = 'email@email.com',
            address = 'direccion prueba',
            medical_history = 'Prueba'
        )

        self.doctor = Doctor.objects.create(
            first_name = 'Juan',
            last_name = 'Espinoza',
            qualification = 'Dentista',
            contact_number = '987654321',
            email = 'doctor@prueba.com',
            address = 'direccion prueba',
            biography = 'un master',
            is_on_vacation = False
        )

        self.client = APIClient()

    
    def test_list_should_return_200(self):
        url = reversed(
            'doctor-appointments',
            kwargs={'pk': self.doctor.id}
            )