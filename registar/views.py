from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewPsicologo
from .models import Psicologo

# Create your views here.

def hello(request):
    return render(request, 'index.html')

def registrar(request):
    if request.method == 'GET':
        #show inteface
        return render(request, 'registrar.html', {
            'form': CreateNewPsicologo()
        })
    else:
        x = 0
        if request.POST['especialidad'] == "cognitiva":
            x = 1
        elif request.POST['especialidad'] == "clinica":
            x = 2
        elif request.POST['especialidad'] == "pareja":
            x = 3
        
        Psicologo.objects.create(rut=request.POST['rut'],nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],password=request.POST['password'], especialidad_id = x)
        return redirect('/exito/')

def update(request):
    if request.method == 'GET':
        return render(request,'updatepsi.html', {
            'form': CreateNewPsicologo(),
            'psicologos': Psicologo.objects.all()
        })
    else:

        x = 0
        if request.POST['especialidad'] == "cognitiva":
            x = 1
        elif request.POST['especialidad'] == "clinica":
            x = 2
        elif request.POST['especialidad'] == "pareja":
            x = 3

        p = Psicologo.objects.get(id=request.POST['psicologo'])
        p.rut = request.POST['rut']
        p.nombre = request.POST['nombre']
        p.apellido = request.POST['apellido']
        p.email = request.POST['email']
        p.password=request.POST['password']
        p.especialidad_id = x
        p.save()
        return redirect('/exito1/')

def exito(request):
    return render(request, 'exito.html')

def exito1(request):
    return render(request, 'exito1.html')


