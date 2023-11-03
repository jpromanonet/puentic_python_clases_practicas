import json
from django.http import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Alumno, Curso
import csv

# Create your views here.
def cargar_alumno(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if csv_file.name.endswith('.csv'):
            try:
                decoded_file = csv_file.read().decode('utf-8')
                csv_data = csv.reader(decoded_file.splitlines(), delimiter=',')
                next(csv_data)  # Skip the header row if it exists

                # Iterate through the CSV data and create or update Alumno objects
                for row in csv_data:
                    dni, nombre, apellido, telefono, correo_electronico, curso_id = row
                    # Perform any necessary data validation and transformation here
                    # For example, you may want to check if the DNI already exists
                    # and handle duplicates accordingly.
                    
                    # Create or update the Alumno object
                    alumno, created = Alumno.objects.update_or_create(
                        dni=dni,
                        defaults={
                            'nombre': nombre,
                            'apellido': apellido,
                            'telefono': telefono,
                            'correo_electronico': correo_electronico,
                            'curso_id': curso_id,
                        }
                    )

                return JsonResponse({'message': 'Alumnos cargados correctamente.'}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'El archivo debe ser un archivo CSV válido.'}, status=400)
    else:
        return JsonResponse({'error': 'Debe proporcionar un archivo CSV para cargar.'}, status=400)

def listar_alumno(request):
    alumnos = Alumno.objects.all()
    
    # Serializa los datos de los alumnos en una lista de diccionarios
    serialized_alumnos = []
    for alumno in alumnos:
        serialized_alumnos.append({
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'dni': alumno.dni,
            'telefono': alumno.telefono,
            'correo_electronico': alumno.correo_electronico,
            'curso': alumno.curso.nombre if alumno.curso else None,
            'banda_horaria': alumno.curso.banda_horaria.nombre if alumno.curso else None,
        })

    # Retorna la respuesta en formato JSON
    return JsonResponse({'alumnos': serialized_alumnos})

def obtener_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni=dni)

    # Serializa los datos del alumno en un diccionario
    serialized_alumno = {
        'nombre': alumno.nombre,
        'apellido': alumno.apellido,
        'dni': alumno.dni,
        'telefono': alumno.telefono,
        'correo_electronico': alumno.correo_electronico,
        'curso': alumno.curso.nombre if alumno.curso else None,
        'banda_horaria': alumno.curso.banda_horaria.nombre if alumno.curso else None,
    }

    # Retorna la respuesta en formato JSON
    return JsonResponse({'alumno': serialized_alumno})


def modificar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni=dni)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))

            # Actualiza los campos del alumno con los datos proporcionados
            alumno.nombre = data.get('nombre', alumno.nombre)
            alumno.apellido = data.get('apellido', alumno.apellido)
            alumno.telefono = data.get('telefono', alumno.telefono)
            alumno.correo_electronico = data.get('correo_electronico', alumno.correo_electronico)
            # Puedes agregar más campos aquí según tus necesidades.

            # Guarda el registro actualizado en la base de datos
            alumno.save()

            return JsonResponse({'message': 'Alumno modificado correctamente.'}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Error en el formato JSON de la solicitud.'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido. Utiliza el método PUT para modificar al alumno.'}, status=405)

def eliminar_alumno(request, dni):
    alumno = get_object_or_404(Alumno, dni=dni)

    if request.method == 'DELETE':
        # Elimina el registro del alumno de la base de datos
        alumno.delete()

        return JsonResponse({'message': 'Alumno eliminado correctamente.'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido. Utiliza el método DELETE para eliminar al alumno.'}, status=405)


def asignar_curso(request, dni, id_curso):
    alumno = get_object_or_404(Alumno, dni=dni)
    curso = get_object_or_404(Curso, id=id_curso)

    if request.method == 'POST':
        # Asigna el curso al alumno
        alumno.curso = curso
        alumno.save()

        return JsonResponse({'message': f'Curso asignado correctamente al alumno con DNI {dni}.'}, status=200)
    else:
        return JsonResponse({'error': 'Método no permitido. Utiliza el método POST para asignar un curso al alumno.'}, status=405)

def alumnos_por_curso(request, id_curso):
    # Filtra los alumnos que están matriculados en el curso específico
    alumnos = Alumno.objects.filter(curso_id=id_curso)

    # Serializa los datos de los alumnos en una lista de diccionarios
    serialized_alumnos = []
    for alumno in alumnos:
        serialized_alumnos.append({
            'nombre': alumno.nombre,
            'apellido': alumno.apellido,
            'dni': alumno.dni,
            'telefono': alumno.telefono,
            'correo_electronico': alumno.correo_electronico,
            # Puedes agregar más campos según tus necesidades.
        })

    # Retorna la respuesta en formato JSON
    return JsonResponse({'alumnos': serialized_alumnos})