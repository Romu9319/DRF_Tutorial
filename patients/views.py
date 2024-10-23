
from .serializers import PatientSerializer
from .models import Patient

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

# método GET -> /api/patients -> listará
# método POST -> /api/patients -> creará
# método GET -> /api/patients/<pk> -> detalles
# método PUT -> /api/patients/<pk> -> modificará
# método DELETE -> /api/patients/<pk> -> borrará


## Vistas vasadas en FUNCIONES 
"""@api_view(['GET','POST']) # debemos añadir el decorador para que DRF sea compatible con la vista, el decorador recibe un 
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
"""

"""@api_view(['GET','PUT', 'DELETE'])
def detail_patient(request, pk): 
    try:    # usamos el try/except en caso de que el usuario pase un id no valido o que no exista
        patient = Patient.objects.get(id=pk)
    except Patient.DoesNotExist:    # en caso de que no exista lanzará el estatus 404_not_found http
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""

## Vistas vasadas en CLASES

# APIView: clase base más fundamental de las CBVs 
"""class ListPatientsView(APIView): # APIView nos da un conjunto de funcionalidades bases, ctrl+left_clic para explorarlas
    allowed_methods = ['GET','POST'] # acá se especifican los métodos con los que trabajara la clase

    def get(self, request): # esta funcion obtiene todos los objetos creados y los serializa para posteriormente mostrarlos serializados 
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self,request): # acá se recibe la información que es enviada por el usuario y serializada, una vez validada la info la guarda en la base de datos
        serializer = PatientSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)"""

class DetailPatientView(APIView):
    allowed_methods = ['GET','PUT', 'DELETE']

    def get(self, request, pk):
        try:    # usamos el try/except en caso de que el usuario pase un id no valido o que no exista
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:    # en caso de que no exista lanzará el estatus 404_not_found http
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        try:    # usamos el try/except en caso de que el usuario pase un id no valido o que no exista
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:    # en caso de que no exista lanzará el estatus 404_not_found http
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        try:    # usamos el try/except en caso de que el usuario pase un id no valido o que no exista
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:    # en caso de que no exista lanzará el estatus 404_not_found http
            return Response(status=status.HTTP_404_NOT_FOUND)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# GenericAPIViews
class ListPatientsView(ListAPIView, CreateAPIView): # APIView nos da un conjunto de funcionalidades bases, ctrl+left_clic para explorarlas
    allowed_methods = ['GET','POST'] # acá se especifican los métodos con los que trabajara la clase
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()