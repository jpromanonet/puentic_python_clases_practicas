from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Alumno
import csv

# Create your views here.
def cargar_alumno(request):
    # Lógica para cargar alumnos desde un archivo CSV
    # Asegurense de manejar adecuadamente la lectura y validación de los archivos .csv

def listar_alumno(request):
    alumnos = Alumno.objects.all()
    # Serializar los datos de los alumnos y retornar una respuesta en formato JSON que ya lo llama desde el modulo django.http

def obtener_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)
    # Resta agregar la logica para hacer un get y traernos el alumno

def modificar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)
    # Resta crear la logica para hacer un push y modificar el registro alumno

def eliminar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni = dni)
    # usar put para eliminar el registro

def asignar_curso(request, dni, id_curso):
    # Logica para asignar un curso a un alumno especifico

def alumnos_por_curso(request, id_curso):
    # Lógica para obtener una lista de alumnes matriculados en un curso especifico.