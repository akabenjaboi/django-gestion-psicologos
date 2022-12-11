from django.urls import path
from . import views

urlpatterns = [
    path('paciente/', views.paciente),
    path('updatepa/', views.update),
    path('exito3/', views.exito3),
    path('exito4/', views.exito4),
]