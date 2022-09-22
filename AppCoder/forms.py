from django import forms


class FormularioEquipo(forms.Form):

    nombre = forms.CharField()
    fechaNacimiento = forms.DateField()
    pais = forms.CharField()
    titulos = forms.IntegerField()
    mejorJugador = forms.CharField()

class FormularioJugador(forms.Form):

    nombre = forms.CharField()
    nacionalidad = forms.CharField()
    edad = forms.IntegerField()
    posicion = forms.CharField()
    dorsal = forms.IntegerField()
    piernaHabil = forms.CharField()

class FormularioEstadio(forms.Form):

    nombre = forms.CharField()
    ubicacion = forms.CharField()
    fechaInauguracion = forms.DateField()
    capacidad = forms.IntegerField()