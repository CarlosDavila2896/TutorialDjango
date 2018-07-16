from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Alumno
from .serializers import AlumnoSerializer

@csrf_exempt
def Alumno_list(request, nivel):
    if request.method == 'GET':
        alumnos = Alumno.objects.filter(Nivel=nivel)
        serializer = AlumnoSerializer(alumnos, many=True)
        return JsonResponse(serializer.data, safe=False)