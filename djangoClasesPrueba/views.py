from contextvars import Context
from pipes import Template
from django.http import HttpRequest, HttpResponse
from datetime import date, datetime
from django.template import Template


def inicio (request):
    return HttpResponse("Hola soy mi primer vista")



def ver_fecha (request):
    fecha_actual = datetime.now()
    return HttpResponse ("Fecha actual {} " .format(fecha_actual)) 

def saludo (request):
    archivo = open (r"C:\Users\agus\OneDrive\Escritorio\Django ch\prueba.html" , "r")
   
    template1 = Template (archivo.read())
    contexto1 = Context ()
    render1 = template1.render (contexto1)
    return HttpResponse ("mi template")