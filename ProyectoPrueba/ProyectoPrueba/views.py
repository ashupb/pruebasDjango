from django. template import Template, Context
from django.http import HttpResponse

def saludar(request):
    saludo = "Bienvenidos al nuevo Proyecto de prueba"
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    saludo = f"Te damos la bienvenida a la comisión 57810 {apellido} {nombre}"
    return HttpResponse(saludo)


def bienvenido_tpl(request):
    with open("C:/Users/apere/OneDrive/Desktop/eLearning/coderhouse/python/Clases/Clase17_Prueba/ProyectoPrueba/ProyectoPrueba/plantillas/bienvenido.html") as miHtml:
        plantilla =Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)
    return HttpResponse(saludo)