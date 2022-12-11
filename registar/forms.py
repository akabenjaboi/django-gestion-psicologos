from django import forms

class CreateNewPsicologo(forms.Form):
    rut = forms.CharField(label="Rut")
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido",max_length=50)
    email = forms.CharField(label="E-mail",max_length=100)
    password = forms.CharField(label="Contraseña",max_length=20)