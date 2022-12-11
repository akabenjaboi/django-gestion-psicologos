from django import forms
from registar.models import Psicologo

class CreateNewAgenda(forms.Form):
    Fecha = forms.DateField()

class CreateNewHora(forms.Form):
    Hora_inicio = forms.TimeField()
    Hora_fin = forms.TimeField()
    