from django.contrib import admin
from .models import Equipo, Campos_de_juego, Patrocinador

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Campos_de_juego)
admin.site.register(Patrocinador)