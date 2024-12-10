from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=50)
    nombre_tecnico = models.CharField(max_length=30)
    jugador1 = models.CharField(max_length=30)
    jugador2 = models.CharField(max_length=30)
    jugador3 = models.CharField(max_length=30)
    jugador4 = models.CharField(max_length=30)
    jugador5 = models.CharField(max_length=30)
    def __str__(self):
        return f"Equipo: {self.nombre_equipo}\nDT: {self.nombre_tecnico}\nJugadores: {self.jugador1}, {self.jugador2}, {self.jugador3}, {self.jugador4}, {self.jugador5}"

class Campos_de_juego(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=40)
    def __str__(self):
        return f"Cancha: {self.nombre} | {self.ubicacion}"
    
class Patrocinador(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return f"Patrocinador: {self.nombre}"