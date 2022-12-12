from django.shortcuts import render
from registar.models import Psicologo
from agenda.models import Agenda, Hora, Agenda_hora
from paciente_info.models import Paciente
from .models import Ah_pac
# Create your views here.


def mostrar_agenda(request, psico, paciente):
    if request.method == 'POST':
        hora = Hora.objects.all()
        psico = request.POST['psicologo']
        print(psico)
        psicologos = Psicologo.objects.all()
        paciente = request.POST['paciente']
        print(paciente)
        agenda = Agenda.objects.filter(psicologo = psico)
        print(agenda)
        horarios = Agenda_hora.objects.all()
        return render(request, 'mostrar_agenda.html', {
            'horarios' : horarios,
            'agendas' : agenda,
            'hora' : hora,
            'psicologos' : psicologos,
            'psicologoID' : int(psico),
            'pacienteID' : paciente
            })
        if request.method == 'POST':
            print("post")
    else:
        print("hola")


    


def ah_pac(request):
    if request.method == 'GET':
        psicologos = Psicologo.objects.all()
        agendas = Agenda.objects.all()
        agenda_hora = Agenda_hora.objects.all()
        hora = Hora.objects.all()
        pacientes = Paciente.objects.all()
        return render(request, 'ah_pac.html',{
            'agendas' : agendas,
            'psicologos' : psicologos,
            'pacientes' : pacientes,
            'agenda_hora' : agenda_hora,
            'hora' : hora
        })
    else:
        psico = request.POST['psicologo']
        print(psico)
        paciente = request.POST['paciente']
        print(paciente)
        return mostrar_agenda(request, psico, paciente,)
        