from django import forms

class CreateNewPaciente(forms.Form):
    rut = forms.CharField(label = "Rut", max_length=13)
    nombre = forms.CharField(label = "Nombre", max_length=50)
    apellido = forms.CharField(label = "Apellido", max_length=50)
    email = forms.CharField(label = "E-mail", max_length=100)
    