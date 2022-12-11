from django.urls import path
from . import views

urlpatterns = [
    path('paciente_ah/', views.ah_pac),
    path('mostrar_agenda/', views.ah_pac),
    path('mostrar_horas/', views.ah_pac)
]