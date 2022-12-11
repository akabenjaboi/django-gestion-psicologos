from django.urls import path
from . import views

urlpatterns = [
    path('agenda/', views.agenda),
    path('exito2/', views.exito2)
]