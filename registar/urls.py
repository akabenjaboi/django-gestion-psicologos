from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.hello),
    path('registrar/', views.registrar),
    path('updatepsi/',views.update, name="update"),
    path('exito/',views.exito),
    path('exito1/',views.exito1)
    
]