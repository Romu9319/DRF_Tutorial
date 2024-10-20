
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# método GET a travez de url /api/patients -> listará
# método POST a travez de url /api/patients -> creará


@api_view(['GET','POST']) # debemos añadir el decorador para que DRF sea compatible con la vista, el decorador recibe un 
                          # parametro el cual indica el método con el que se va a ejecutar el endpoint

def list_patients(request): # la variable request en la función list_patients representa la solicitud HTTP que se recibe al acceder al endpoint correspondiente
    if request.method == 'GET':
        patients = Patient.objects.all() # asigno dentro de la variable patients el listado 
                                     # con todos los pacientes pertenecientes al modelo Patients                                     
        serializer = PatientSerializer(patients, many=True) # le paso los pasientes al serializer(PatientSerializer), como este solo 
                                                        # puede serializar un objeto por vez se configura con el parámetro 
                                                        # many=True para que utilice el mismo serializer para cada objeto de la lista 
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PatientSerializer(data = request.data) # le pasamos a PatientSerializer la informacione que 
                                                            # queremos serializar a travez del request.data,el cual
                                                            # contiene la informacion enviadad desde cliente 
        serializer.is_valid(raise_exception=True)   # hacemos la validación del serializdor y con raise_exeception=true
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    
@api_view(['GET','PUT'])
def detail_patient(request, pk): 
    if request.method == 'GET':
        try:    # usamos el try/except en caso de que el usuario pase un id no valido o que no exista
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:    # en caso de que no exista lanzará el estatus 404_not_found http
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)