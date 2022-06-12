from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from AppCoder.models import  Curso, Profesor, Estudiante
from django.template import loader
from AppCoder.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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
@login_required
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

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#LISTVIEWS
class EstudiantesList(LoginRequiredMixin, ListView):
     model = Estudiante
     template_name = 'AppCoder/estudiante_list.html'

#DETAILVIEWS
class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_detalle.html'

#CREATEVIEWS
class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']

#UPDATEVIEWS
class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')
    fields = ['nombre', 'apellido', 'email']

#DELETEVIEWS
class EstudianteEliminacion(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_list')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#LOGIN
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            #Autentificacion de usuario
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido capo {usuario}'})
            else:
                return render(request, 'AppCoder/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos.'})
        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje': 'El usuario no existe.'})
    else:
        form = AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'form':form})

#REGISTRO
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado con exito.'})
        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje': 'Error, no se pudo crear el usuario.'})           
    else:
        form = UserRegistrationForm()
        return render(request, 'AppCoder/register.html', {'form':form})
