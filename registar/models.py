from django.db import models

# Create your models here.

class Especialidad(models.Model):
    esp_nombre = models.CharField(max_length=50)
    esp_descripcion = models.CharField(max_length=500)

class Psicologo(models.Model):
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)