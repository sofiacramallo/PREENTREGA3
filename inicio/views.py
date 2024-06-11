from django.shortcuts import render
#from AppCoder.models import Curso
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import random
# Create your views here.
def inicio(request):
    return HttpResponse("vista inicio")
def template1(request, nombre, apellido):
    fecha = datetime.now()
    return HttpResponse(f"<h1>Mi template </h1>-- Fecha: {fecha} -- Buenas {nombre} {apellido}")
def template2(request, nombre, apellido):
    archivo_abierto = open(r'C:\Users\ramal\Desktop\ProyectoFinal\PreentregaTres\template\template2.html')
    fecha = datetime.now()
    template= Template(archivo_abierto.read())
    archivo_abierto.close()
    datos= {'fecha': fecha, 'nombre': nombre, 'apellido': apellido}
    contexto = Context(datos)
    template_renderizado= template.render(contexto)

    return HttpResponse(template_renderizado)
def template3(request, nombre, apellido):
    #archivo_abierto = open(r'C:\Users\ramal\Desktop\ProyectoFinal\PreentregaTres\template\template2.html')
    #template= Template(archivo_abierto.read())
    #archivo_abierto.close()
    template= loader.get_template('template2.html') #esste reemplaza los tres codigos de arriba
    fecha = datetime.now()
    datos= {'fecha': fecha, 'nombre': nombre, 'apellido': apellido}
    #contexto = Context(datos) #tampoco necesito este con el loader
    template_renderizado= template.render(datos)

    return HttpResponse(template_renderizado)
def template4(request, nombre, apellido): #este es el más optimizado
    fecha = datetime.now()
    datos= {'fecha': fecha, 'nombre': nombre, 'apellido': apellido}
    return render(request, 'template2.html', datos)
def probando(request):
    lista= list(range(500))
    numeros= random.choices(lista, k=50)
    return render(request, 'probando_if_for.html', {'numeros': numeros})
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