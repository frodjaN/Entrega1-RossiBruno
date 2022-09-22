from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.forms import FormularioEquipo, FormularioEstadio, FormularioJugador
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.


def inicio(request):

    return render(request, "AppCoder/inicio.html")


def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioEquipo(request.POST)


        if formulario1.is_valid(): 

            info = formulario1.cleaned_data

            equipo = EquipoDeFutbol(nombre=info["nombre"], fechaNacimiento=info["fechaNacimiento"], pais=info["pais"], titulos=info["titulos"], mejorJugador=info["mejorJugador"]) 

            equipo.save() 

            return render(request, "AppCoder/inicio.html")

    else:
        formulario1=FormularioEquipo()


    return render(request, "AppCoder/formularioEquipo.html", {"formularioEquipo":formulario1}) 

def formulario2(request):

    if request.method=="POST":
        
        formulario2 = FormularioJugador(request.POST)


        if formulario2.is_valid(): 

            info = formulario2.cleaned_data

            jugador = JugadorFutbol(nombre=info["nombre"], nacionalidad=info["nacionalidad"], edad=info["edad"], posicion=info["posicion"], dorsal=info["dorsal"], piernaHabil=info["piernaHabil"])

            jugador.save() 

            return render(request, "AppCoder/inicio.html")

    else:
        formulario2=FormularioJugador() 


    return render(request, "AppCoder/formularioJugador.html", {"formularioJugador":formulario2}) 


def formulario3(request):

    if request.method=="POST":

        formulario3 = FormularioEstadio(request.POST)


        if formulario3.is_valid():

            info = formulario1.cleaned_data

            estadio = EstadioFutbol(nombre=info["nombre"], ubicacion=info["ubicacion"], fechaInauguracion=info["fechaInauguracion"], capacidad=info["capacidad"])

            estadio.save() 

            return render(request, "AppCoder/inicio.html") 

    else:
        formulario3=FormularioEstadio() 

    return render(request, "AppCoder/formularioEstadio.html", {"formularioEstadio":formulario3}) 



def busqueda(request):

    return render(request, "AppCoder/busqueda.html")

def busquedaEstadio(request):

    return render(request, "AppCoder/busquedaEstadio.html")

def busquedaEquipo(request):

    return render(request, "AppCoder/busquedaEquipo.html")


'''
def buscar(request):

    respuesta= f"Estoy buscando la camada nro: {request.GET['camada']}"

    return HttpResponse(respuesta)
'''


def buscar(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        jugadores = JugadorFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultados.html", {"jugadores":jugadores, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)

def buscarEquipo(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        equipos = EquipoDeFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultadosEquipo.html", {"equipos":equipos, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)

def buscarEstadio(request):

    if request.GET["nombre"]:

        busqueda = request.GET["nombre"]
        estadios = EstadioFutbol.objects.filter(nombre__icontains=busqueda)

        return render(request, "AppCoder/resultadosEstadio.html", {"estadios":estadios, "busqueda":busqueda})
    else:

        mensaje = "No enviaste datos."   

    return HttpResponse(mensaje)
