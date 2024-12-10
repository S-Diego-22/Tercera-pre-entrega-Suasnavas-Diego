from django import forms

class EquiposFormularios(forms.Form):
    nombre_equipo = forms.CharField(max_length=50)
    nombre_dt = forms.CharField(max_length=30)
    jugador1 = forms.CharField(max_length=30)
    jugador2 = forms.CharField(max_length=30)
    jugador3 = forms.CharField(max_length=30)
    jugador4 = forms.CharField(max_length=30)
    jugador5 = forms.CharField(max_length=30)

class Campo_de_juegoFormularios(forms.Form):
    nombre = forms.CharField(max_length=30)
    ubicacion = forms.CharField(max_length=40)

class PatrocinadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=15)