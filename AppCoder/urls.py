
from django.urls import path
from AppCoder.views import *


urlpatterns = [
    path('curso/', curso),
    path('', inicio, name = "Inicio"),
    path('cursos/', cursos, name = "Cursos"),
    path('estudiantes/', estudiantes, name = "Estudiantes"),
    path('entregables/', entregables, name = "Entregables"),
    path('cursoFormulario/', cursoFormulario, name = "cursoFormulario"),
    path('profesorFormulario/', profesorFormulario, name = "profesorFormulario"),
    path('busquedaCamada/', busquedacamada, name = "BusquedaCamada"),
    path('buscar/', buscar, name = "buscar"),
    path('profesores/', leerProfesores, name = "Profesores"),
]
