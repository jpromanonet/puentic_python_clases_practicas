# Creamos una función para calcular promedios
def calcular_promedios(diccionario_estudiantes):
    promedios = {} # Creamos un diccionario vacio para almacenar los promedios

    # Recorremos las notas para calcular los promedios
    for estudiante, notas in diccionario_estudiantes.items():
        try:
            # Calculamos el promedio de las notas del estudiante
            promedio = sum(notas) / len(notas)
            promedios[estudiante] = promedio
        except ZeroDivisionError:
            # Manejamos el caso en que la lista de notas este vacia
            promedios[estudiante] = 0
        except TypeError:
            # manejamos notas que no son numeros
            promedios[estudiante] = "Notas no validas"

    return promedios

# Veamos un ejemplo de uso
diccionario_estudiantes = {
    "Juan P.": [9,9,9],
    "Estela": [9,9,9],
    "Alejandro": [9,9,8]
}

print(diccionario_estudiantes)
print(" ")

promedios = calcular_promedios(diccionario_estudiantes)
print(promedios)