from django.db import models


class Nivel(models.Model):
    Nombre = models.CharField(max_length=100)


class Alumno(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)