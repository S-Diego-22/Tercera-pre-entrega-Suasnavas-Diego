from django.shortcuts import render, redirect
from .forms import Campo_de_juegoFormularios, EquiposFormularios, PatrocinadoresFormulario
from .models import Equipo, Campos_de_juego, Patrocinador

# Create your views here.

# views del menú
def inicio(request):
    return render(request, "app_pagina/index.html")

def equipos(request):
    query = request.GET.get("q")
    if query:
        equipo = Equipo.objects.filter(nombre_equipo__icontains = query)
    else:
        equipo = Equipo.objects.all()
    return render(request, "app_pagina/equipos.html", {"equipo": equipo})

def campo_de_juego(request):
    query = request.GET.get("q")
    if query:
        campo = Campos_de_juego.objects.filter(nombre__icontains = query)
    else:
        campo = Campos_de_juego.objects.all()
    return render(request, "app_pagina/campo_de_juego.html", {"campo": campo})

def patrocinadores(request):
    query = request.GET.get("q")
    if query:
        patrocinador = Patrocinador.objects.filter(nombre__icontains = query)
    else:
        patrocinador = Patrocinador.objects.all()
    return render(request, "app_pagina/patrocinadores.html", {"patrocinador": patrocinador})

# views de los formularios

def equipos_formulario(request):
    if request.method == "POST":
        formulario = EquiposFormularios(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            equipo = Equipo(nombre_equipo = informacion["nombre_equipo"], 
                             nombre_tecnico = informacion["nombre_dt"], 
                             jugador1 = informacion["jugador1"],
                             jugador2 = informacion["jugador2"],
                             jugador3 = informacion["jugador3"],
                             jugador4 = informacion["jugador4"],
                             jugador5 = informacion["jugador5"])
            equipo.save()
            return redirect("equipos")        
    else:
        formulario = EquiposFormularios()
    
    return render(request, "app_pagina/forms/formulario_equipos.html", {"formulario": formulario})

def campo_formularios(request):
    if request.method == "POST":
        formulario = Campo_de_juegoFormularios(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            campo = Campos_de_juego(nombre = informacion["nombre"],
                                    ubicacion = informacion["ubicacion"])
            campo.save()
            return redirect("campo de juego")
    else:
        formulario = Campo_de_juegoFormularios()

    return render(request, "app_pagina/forms/formulario_campo.html", {"formulario": formulario})

def patrocinador_formulario(request):
    if request.method == "POST":
        formulario = PatrocinadoresFormulario(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            patrocinador = Patrocinador(nombre = informacion["nombre"])
            patrocinador.save()
            return redirect("patrocinadores")
    else:
        formulario = PatrocinadoresFormulario()
    
    return render(request, "app_pagina/forms/formulario_patrocinador.html", {"formulario": formulario})