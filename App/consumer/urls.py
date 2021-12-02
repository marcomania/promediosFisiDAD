from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('',views.home),
    path('verAlumnos/',views.AlumnosH),
    path('verCursos/',views.CursosH),
    path('registrarCurso/',views.registrarCurso),
    path('eliminarCurso/<codcur>',views.eliminarCurso),
    path('modificarCurso/<codcur>',views.modificarCurso),
    path('editarCurso/',views.editarCurso),
    path('registrarAlumno/',views.registrarAlumno),
    path('eliminarAlumno/<codalu>',views.eliminarAlumno),
    path('modificarAlumno/<codalu>',views.modificarAlumno),
    path('editarAlumno/',views.editarAlumno),
    path('PromediosAlumno/<codalu>',views.PromediosAlumno),
]