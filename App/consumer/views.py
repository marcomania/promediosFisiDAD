from django.shortcuts import redirect, render
from .models import AluCur, Alumno, Curso
from django.db.models import Avg, Sum

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    return render(request,"gestionCursos.html", {"cursos":cursosListados})

def AlumnosH(request):
    alumnosListados = Alumno.objects.all()
    return render(request,"gestionAlumnos.html", {"alumnos":alumnosListados})

def CursosH(request):
    cursosListados = Curso.objects.all()
    return render(request,"gestionCursos.html", {"cursos":cursosListados})

###############################################################################

def registrarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credit=request.POST['numCredit']

    curso=Curso.objects.create(codcur=codigo, nomcur=nombre, credcur=credit)

    return redirect('/verCursos')

def eliminarCurso(request, codcur):
    curso = Curso.objects.get(codcur=codcur)
    curso.delete()

    return redirect('/verCursos')

def modificarCurso(request, codcur):
    curso = Curso.objects.get(codcur=codcur)
    return render(request, "modificarCurso.html", {"curso":curso})

def editarCurso(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    credit=request.POST['numCredit']


    curso = Curso.objects.get(codcur=codigo)
    curso.nomcur = nombre
    curso.credcur = credit
    curso.save()

    return redirect('/verCursos')


def registrarAlumno(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apelli=request.POST['txtApellido']

    alumno=Alumno.objects.create(codalu=codigo, nomalu=nombre, apealu=apelli)

    return redirect('/verAlumnos')

def eliminarAlumno(request, codalu):
    alumno = Alumno.objects.get(codalu=codalu)
    alumno.delete()

    return redirect('/verAlumnos')

def modificarAlumno(request, codalu):
    alumno = Alumno.objects.get(codalu=codalu)
    return render(request, "modificarAlumno.html", {"alumno":alumno})

def editarAlumno(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apelli=request.POST['txtApellido']


    alumno = Alumno.objects.get(codalu=codigo)
    alumno.nomalu = nombre
    alumno.apealu = apelli
    alumno.save()

    return redirect('/verAlumnos')

def PromediosAlumno(request, codalu):
    alucur = AluCur.objects.filter(codalu=codalu)
    return render(request, "PromediosAlumno.html", {"alucur":alucur})