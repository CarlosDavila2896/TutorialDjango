from rest_framework import serializers
from .models import Alumno

class AlumnoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    Nombre = serializers.CharField(max_length=50)
    Apellido = serializers.CharField(max_length=50)
    Nivel = serializers.SlugRelatedField(slug_field='Nombre', read_only=True)
