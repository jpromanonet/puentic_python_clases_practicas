from django.db import models

# Create your models here.
class BandaHoraria(models.Model): # 1.a
    nombre = models.CharField(max_length=255)
    horario_inicio = models.DateTimeField()
    horario_fin = models.DateTimeField()

class Curso(models.Model): # 1.b
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    banda_horaria = models.ForeignKey(BandaHoraria, on_delete=models.CASCADE)
    nota = models.IntegerField()

class Alumno(models.Model): # 1.c
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField(primary_key=True)
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)