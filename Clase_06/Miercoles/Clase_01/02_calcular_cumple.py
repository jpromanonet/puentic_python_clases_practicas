# Importamos el modulo datetime
from datetime import datetime

# Creamos una funcion que calcule cuanto falta para el proximo cumpleaños
def calcular_tiempo_proximo_cumple(fecha_cumple):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Convertimos la fecha de cumpleaños proporcionada por el usuario en un objeto datetime
    fecha_cumple = datetime.strptime(fecha_cumple, '%d/%m/%Y')

    # Calcular la fecha del próximo cumpleaños
    año_actual = fecha_actual.year
    proximo_cumple = fecha_cumple.replace(year=año_actual)

    # Verificar si el próximo cumpleaños ya ocurrio este año y si es así, calcular para el proximo
    if fecha_actual > proximo_cumple:
        proximo_cumple = fecha_cumple.replace(year = año_actual + 1)
    
    # Calcular la diferencia del tiempo hasta el proximo cumple
    tiempo_faltante = proximo_cumple - fecha_actual

    return tiempo_faltante

if __name__ == "__main__":
    fecha_cumple = input("Ingrese su fecha de cumpleaños (dd/mm/aaaa): ")

    try:
        tiempo_faltante = calcular_tiempo_proximo_cumple(fecha_cumple)
        dias_faltantes = tiempo_faltante.days
        print(f'Faltan {dias_faltantes} días para su proximo cumpleaños.')
    except ValueError:
        print('Formato de fecha incorrento. Utlice dd/mm/aaaa.')