from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateNewAgenda, CreateNewHora
from registar.models import Psicologo
from .models import Agenda, Hora, Agenda_hora
# Create your views here.

def agenda(request):
    if request.method == 'GET':
        psicologos = Psicologo.objects.all()
        return render(request, 'agenda.html', {
            'form': CreateNewAgenda(),
            'psicologos' : psicologos, 
            'form_date' : CreateNewHora()})
    else:
        a_object = Agenda.objects.create(psicologo_id=int(request.POST['psicologo']), agenda_fecha=request.POST['Fecha']) 

        a_object.save()

        h_object = Hora.objects.create(hora_inicio=request.POST['Hora_inicio'],hora_fin = request.POST['Hora_fin'])

        h_object.save()
        
        print(a_object.pk)
        print(h_object.pk)

        Agenda_hora.objects.create(agenda = a_object, hora = h_object)

        return redirect('/exito2/')

def exito2(request):
    return render(request, 'exito2.html')