from django.db import models

# Create your models here.

class Region(models.Model):
    Reg_nombre = models.CharField(max_length=50)
    
    
class Paciente(models.Model):
    rut = models.CharField(max_length=13)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null = True)