from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import  Curso, Profesor
from django.template import loader
from AppCoder.forms import *

# Create your views here.

def curso(self):
    curso = Curso(nombre='Desarrollo web', camada=25802)
    curso.save()

    documento= f"Curso: {curso.nombre} - Camada: {curso.camada}"
    return HttpResponse(documento)

def profesores(request):
    return render (request, 'appCoder/profesores.html')

def estudiantes(request):
    return render (request, 'appCoder/estudiantes.html')

def entregables(request):
    return render (request, 'appCoder/entregables.html')

def cursos(request):
    return render (request, 'appCoder/cursos.html')

def inicio(self):
    plantilla = loader.get_template('appCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def cursoFormulario(request):
    if request.method == "POST":
        miformulario = CursoFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
        nombre = informacion['curso']
        camada = informacion['camada']
        curso = Curso(nombre=nombre, camada = camada)
        curso.save()
        return render(request, "appCoder/inicio.html")
    else:
        miformulario = CursoFormulario()
    return render (request, 'AppCoder/cursoFormulario.html', {"miformulario":miformulario})


def busquedacamada(request):
    return render(request, 'appCoder/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada=camada)
        return render(request, "appCoder/resultadoBusqueda.html", {"curso":curso,"camada":camada})
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

#CRUD Read
def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render(request, 'AppCoder/profesores.html', contexto)

#CRUD Create
def profesorFormulario(request):
    if request.method == "POST":
        miformulario = ProfesorFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
        nombre = informacion['nombre']
        apellido = informacion['apellido']
        email = informacion['email']
        profesion = informacion['profesion']
        profesor = Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
        profesor.save()
        return render(request, "appCoder/inicio.html")
    else:
        miformulario = ProfesorFormulario()
    return render(request, "AppCoder/profesorFormulario.html", {"miformulario":miformulario})

#CRUD Delete
def eliminarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {'profesores':profesores}
    return render(request, 'AppCoder/profesores.html', contexto)

#CRUD Update
def editarProfesor(request, nombre):
    profesor = Profesor.objects.get(nombre=nombre)
    if request.method == "POST":
        miformulario = ProfesorFormulario(request.POST)
        if miformulario.is_valid():
            informacion = miformulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()

            profesores = Profesor.objects.all()
            contexto = {'profesores':profesores}
            return render(request, 'AppCoder/profesores.html', contexto)
    else:
        miformulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
        contexto = {'miformulario':miformulario, 'nombre':nombre}
        return render(request, 'AppCoder/editarProfesores.html', contexto)

