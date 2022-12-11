from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewPaciente
from .models import Paciente
# Create your views here.

def paciente(request):
    if request.method == 'GET':
        #show inteface
        return render(request, 'paciente.html', {
            'form': CreateNewPaciente()
        })
    else:
        x = 0
        if request.POST['region'] == "1":
            x = 1
        elif request.POST['region'] == "2":
            x = 2
        elif request.POST['region'] == "3":
            x = 3
        elif request.POST['region'] == "4":
            x = 4
        elif request.POST['region'] == "5":
            x = 5
        elif request.POST['region'] == "6":
            x = 6
        elif request.POST['region'] == "7":
            x = 7
        elif request.POST['region'] == "8":
            x = 8
        elif request.POST['region'] == "9":
            x = 9
        elif request.POST['region'] == "10":
            x = 10
        elif request.POST['region'] == "11":
            x = 11
        elif request.POST['region'] == "12":
            x = 12
        elif request.POST['region'] == "13":
            x = 13
        elif request.POST['region'] == "14":
            x = 14
        elif request.POST['region'] == "15":
            x = 15
        elif request.POST['region'] == "16":
            x = 16

        Paciente.objects.create(rut=request.POST['rut'],nombre=request.POST['nombre'],apellido=request.POST['apellido'],email=request.POST['email'],region_id = x)
        return redirect('/exito3/')

def update(request):
    if request.method == 'GET':
        return render(request,'updatepa.html', {
            'form': CreateNewPaciente(),
            'pacientes': Paciente.objects.all()
        })
    else:
        x = 0
        if request.POST['region'] == "1":
            x = 1
        elif request.POST['region'] == "2":
            x = 2
        elif request.POST['region'] == "3":
            x = 3
        elif request.POST['region'] == "4":
            x = 4
        elif request.POST['region'] == "5":
            x = 5
        elif request.POST['region'] == "6":
            x = 6
        elif request.POST['region'] == "7":
            x = 7
        elif request.POST['region'] == "8":
            x = 8
        elif request.POST['region'] == "9":
            x = 9
        elif request.POST['region'] == "10":
            x = 10
        elif request.POST['region'] == "11":
            x = 11
        elif request.POST['region'] == "12":
            x = 12
        elif request.POST['region'] == "13":
            x = 13
        elif request.POST['region'] == "14":
            x = 14
        elif request.POST['region'] == "15":
            x = 15
        elif request.POST['region'] == "16":
            x = 16

        p = Paciente.objects.get(id=request.POST['paciente'])
        p.rut = request.POST['rut']
        p.nombre = request.POST['nombre']
        p.apellido = request.POST['apellido']
        p.email = request.POST['email']
        p.region_id = x
        p.save()
        return redirect('/exito4/')

def exito3(request):
    return render(request, 'exito3.html')

def exito4(request):
    return render(request, 'exito4.html')

