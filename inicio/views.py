from django.shortcuts import render, redirect
#from AppCoder.models import Curso
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
import random
from inicio.models import Curso, Profesor, Entregable, Auto, Alumno
from inicio.forms import cargarAlumnoFormulario
# Create your views here.
def inicio(request):
    return render(request, 'inicio/index.html')
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
def curso(self):
    curso= Curso(nombre="Desarrollo Web", camada= "19881")
    curso.save()
    documentoDeTexto= f"Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto) 
#def crear_auto(request):
#    print(request)
#    print(request.GET)
#    print(request.POST)
#    formulario = crearAutoFormulario()
#    if request.method == 'POST':
#        formulario = crearAutoFormulario(request.POST)
#        if formulario.is_valid():
#            datos= formulario.cleaned_data
#            auto =Auto(marca=datos.get('marca'), modelo=datos.get('modelo'))
#            auto.save()
#            return redirect('autos')
#    return render(request, 'curso.template/cursoTemplate.html', {'formulario': formulario})
def alumnos(request):
    alumnos= Alumno.objects.all()
    return render(request, 'inicio/alumnos.html', {'alumnos': alumnos})
def cargar_alumno(request):
    print(request)
    print(request.GET)
    print(request.POST)
    formulario = cargarAlumnoFormulario()
    if request.method == 'POST':
        formulario = cargarAlumnoFormulario(request.POST)
        if formulario.is_valid():
            datos= formulario.cleaned_data
            alumno =Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
            alumno.save()
            return redirect('alumnos')
    return render(request, 'curso.template/cursoTemplate.html', {'formulario': formulario})

#render(request, 'curso.template/cursoTemplate.html', {"auto"=auto})
#ejemplo de clase 19 el ejemplo con auto es
#return render(request, 'acá iria el template', {'auto'= auto})
#como el template lo cree en una carpeta sería por ejemplo 'curso.template/cursoTemplate.html'
def profesores(request):
    return HttpResponse("vista profesores")
#def estudiantes(request):
#    return HttpResponse("vista estudiantes")
def entregables(request):
    return HttpResponse("vista entregables")