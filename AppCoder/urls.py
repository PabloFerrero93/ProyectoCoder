
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
    path('eliminarprofesores/<nombre>', eliminarProfesor, name = "eliminarProfesor"),
    path('editarprofesor/<nombre>', editarProfesor, name = "editarProfesor"),
    #----------------------------------------------------------------------------------------------------------
    path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_list'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/create/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/edicion/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),
]
