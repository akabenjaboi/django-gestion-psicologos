from django.db import models
from registar.models import Psicologo 
# Create your models here.

class Agenda(models.Model):
    psicologo = models.ForeignKey(Psicologo, on_delete = models.CASCADE)
    agenda_fecha = models.DateField()

class Hora(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

class Agenda_hora(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete = models.CASCADE)
    hora = models.ForeignKey(Hora, on_delete = models.CASCADE)