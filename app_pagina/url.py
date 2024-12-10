from django.urls import path
from app_pagina.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("equipos/", equipos, name= "equipos"),
    path("campo de juego/", campo_de_juego, name= "campo de juego"),
    path("patrocinadores/", patrocinadores, name= "patrocinadores"),

    # url de los formularios

    path("formulario-equipos/",equipos_formulario, name= "formulario-equipos"),
    path("formulario-campo/", campo_formularios, name= "formulario-campo"),
    path("formulario-patrocinador/", patrocinador_formulario, name= "formulario-patrocinador")
]
