# Creamos una función para calcular promedios
def calcular_promedios(diccionario_estudiantes):
    promedios = {} # Creamos un diccionario para almacenar los promedios

    # Recorremos las notas para calcular los promedios
    for estudiante, notas in diccionario_estudiantes.items():
        try:
            # Calculamos el promedio de la snotas del estudiante
            promedio = sum(notas) / len(notas)
            promedios[estudiante] = round(promedio)
        except ZeroDivisionError:
            # Manejamos el caso en que la lista de notas esté vacia
            promedios[estudiante] = 0
        except TypeError:
            # Devolvemos error si la nota no es un numero valido
            promedios[estudiante] = "Notas no validas"
    
    return promedios

# Ejemplo de uso:
diccionario_estudiantes = {
    "Estudiante1": [8,9,7],
    "Estudiante2": [9,8,9],
    "Estudiante3": [7,8,6]
}
print(diccionario_estudiantes)

promedios = calcular_promedios(diccionario_estudiantes)
print(promedios)