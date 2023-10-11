# Importamos el modulo datetime
from datetime import datetime

# Creamos una función que calcule cuanto falta para el proximo cumpleaños
def calcular_proximo_cumpleaños(fecha_cumpleaños):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Convertimos la fecha de cumpleaños en un objeto datetime
    fecha_cumpleaños = datetime.strptime(fecha_cumpleaños, '%d/%m/%Y')

    # Calcular la fecha del proximo cumpleaños
    año_actual = fecha_actual.year
    proximo_cumpleaños = fecha_cumpleaños.replace(year = año_actual)

    # Verificar si el proximo cumpleaños ya ocurrio este año y si es asi, calcular para el proximo
    if fecha_actual > proximo_cumpleaños:
        proximo_cumpleaños = fecha_cumpleaños.replace(year = año_actual + 1)
    
    # Calcular la diferencias del tiempo hasta el proximo cumpleaños
    tiempo_faltante = proximo_cumpleaños - fecha_actual