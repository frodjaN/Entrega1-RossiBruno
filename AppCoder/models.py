from django.db import models

# Create your models here.

class EquipoDeFutbol(models.Model):

    nombre = models.CharField(max_length=60)
    fechaNacimiento = models.DateField()
    pais = models.CharField(max_length=60)
    titulos = models.PositiveIntegerField(default=0)
    mejorJugador = models.CharField(max_length=60)

class JugadorFutbol(models.Model):
    nombre = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=60)
    edad = models.PositiveIntegerField(default=0)
    posicion = models.CharField(max_length=60)
    dorsal = models.PositiveIntegerField(default=0)
    piernaHabil = models.CharField(max_length=60)

class EstadioFutbol(models.Model):
    nombre = models.CharField(max_length=60)
    ubicacion = models.CharField(max_length=60)
    fechaInauguracion = models.DateField()
    capacidad = models.PositiveIntegerField(default=0)
