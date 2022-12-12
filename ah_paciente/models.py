from django.db import models
from agenda.models import Agenda_hora
from paciente_info.models import Paciente
from registar.models import Psicologo
# Create your models here.

class Ah_pac(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete = models.CASCADE, null = True)
    reservada = models.BooleanField(default=False)
    confirmada = models.BooleanField(default=False)
    
    online = models.BooleanField(default=False)
    link = models.CharField(max_length=800)
    valoracion = models.IntegerField(null = True)
    psicologo = models.ForeignKey(Psicologo, on_delete = models.CASCADE, null = True)
    agenda = models.ForeignKey(Agenda_hora, on_delete = models.CASCADE, null = True)