# Creamos una función para calcular promedios
def calcular_promedios(diccionario_estudiantes):
    promedios = {} # Creamos un diccionario para almacenar los promedios

    # Recorremos las notas para calcular los promedios
    for estudiante, notas in diccionario_estudiantes.items():
        try:
            # Calculamos el promedio de las notas de cada estudiante
            promedio = sum(notas) / len(notas)
            promedios[estudiante] = promedio
        except (ZeroDivisionError, TypeError):
            promedios[estudiante] = "No se puede calcular la nota"
        '''
        except ZeroDivisionError:
            # Manejamos el caso en que la lista de notas esté vacia
            promedios[estudiante] = 0
        except TypeError:
            # Devolvemos un error en caso de que la nota no sea un número valido
            promedios[estudiante] = "Notas no validas"
        '''
    return promedios

# Caso de uso
diccionario_estudiantes = {
    "Estudiante1": [9,8,7],
    "Estudiante2": [9,9,8],
    "Estudiante3": [7,7,7],
    "Estudiante4": ["Ausente", 0, 5, 6]
}

print(diccionario_estudiantes)

# Ejecutar e imprimir en pantalla los promedios
promedios = calcular_promedios(diccionario_estudiantes)
print(promedios)