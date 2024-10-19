
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"]) # debemos añadir el decorador para que DRF sea compatible con la vista, el decorador recibe un 
                   # parametro el cual indica el método con el que se va a ejecutar el endpoint
def list_patients(request):
    patients = Patient.objects.all() # asigno dentro de la variable patients el listado 
                                     # con todos los pacientes pertenecientes al modelo Patients                                     
    serializer = PatientSerializer(patients, many=True) # le paso los pasientes al serializer(PatientSerializer), como este solo 
                                                        # puede serializar un objeto por vez se configura con el parámetro 
                                                        # many=True para que utilice el mismo serializer para cada objeto de la lista 
    return Response(serializer.data)