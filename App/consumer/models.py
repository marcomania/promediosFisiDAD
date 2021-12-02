from django.db import models

# Create your models here.
class Curso(models.Model):
    codcur=models.CharField(primary_key=True,max_length=8)
    nomcur=models.CharField(max_length=50)
    credcur=models.PositiveSmallIntegerField()
    def __str__(self):
        return str(self.nomcur)

class Alumno(models.Model):
    codalu=models.CharField(primary_key=True,max_length=8)
    nomalu=models.CharField(max_length=50)
    apealu=models.CharField(max_length=50)
    def __str__(self):
        return str(self.nomalu)

class AluCur(models.Model):
    codalu=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    codcur=models.ForeignKey(Curso, on_delete=models.CASCADE)
    notacur=models.IntegerField(default=4)