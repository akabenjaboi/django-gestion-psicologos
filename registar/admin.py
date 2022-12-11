from django.contrib import admin

# Register your models here.
from .models import Especialidad
from .models import Psicologo



admin.site.register(Especialidad)
admin.site.register(Psicologo)