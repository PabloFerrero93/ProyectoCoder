
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


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
    #----------------------------------------------------------------------------------------------------------
    #Login and register
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'AppCoder/logout.html'), name='logout'),
]
