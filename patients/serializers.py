from datetime import date
from rest_framework import serializers

from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializer

class PatientSerializer(serializers.ModelSerializer):

    appointments = AppointmentSerializer(many=True, read_only=True)

    age = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'age',
            'date_of_birth',
            'contact_number',
            'email',
            'address',
            'medical_history',
            'appointments',
        ]

    def get_age(self, obj):
       patient_age = date.today() - obj.date_of_birth
       years = patient_age.days // 365
       return f"{years}"
    

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'