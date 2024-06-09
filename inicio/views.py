from django.shortcuts import render
#from AppCoder.models import Curso
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")
def template1(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Mi template </h1>-- Fecha: {fecha} -- Buenas {nombre} {apellido}")
def template2(request, nombre, apellido):
    archivo_abierto = open(r'C:\Users\ramal\Desktop\ProyectoFinal\PreentregaTres\template\template2.html')
    template= Template(archivo_abierto.read())
    archivo_abierto.close()
    contexto = Context()
    template_renderizado= template.render(contexto)

    return HttpResponse(template_renderizado)

#def curso(self):
#    curso= Curso(nombre="Desarrollo Web", camada= "19881")
#    curso.save()
#    documentoDeTexto= f"Curso: {curso.nombre} Camada: {curso.camada}"
 #  return HttpResponse(documentoDeTexto)
#def profesores(request):
 #   return HttpResponse("vista profesores")
#def estudiantes(request):
 #   return HttpResponse("vista estudiantes")
#def entregables(request):
 #   return HttpResponse("vista entregables")