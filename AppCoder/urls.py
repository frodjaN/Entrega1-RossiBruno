from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path("equipo/", formulario1, name="form1"),
    path("jugador/", formulario2, name="form2"),
    path("estadio/", formulario3, name="form3"),
    path("busqueda", busqueda, name="Buscar"),
    path("busquedaEquipo", busquedaEquipo, name="BuscarEquipo"),
    path("busquedaEstadio", busquedaEstadio, name="BuscarEstadio"),
    path("buscar/", buscar),
    path("buscarEquipo/", buscarEquipo),
    path("buscarEstadio/", buscarEstadio),
]