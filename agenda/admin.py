from django.contrib import admin

# Register your models here.

from .models import Agenda
from .models import Agenda_hora
from .models import Hora

admin.site.register(Agenda)
admin.site.register(Agenda_hora)
admin.site.register(Hora)