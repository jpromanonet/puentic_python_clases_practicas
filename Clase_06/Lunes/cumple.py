from datetime import datetime

def calcular_tiempo_hasta_cumpleaños(fecha_cumpleaños):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Convertir la fecha de cumpleaños proporcionada por el usuario en un objeto datetime
    fecha_cumpleaños = datetime.strptime(fecha_cumpleaños, '%d/%m/%Y')

    # Calcular la fecha del próximo cumpleaños
    año_actual = fecha_actual.year
    proximo_cumpleaños = fecha_cumpleaños.replace(year=año_actual)

    # Verificar si el próximo cumpleaños ya ocurrió este año y si es así, calcular para el próximo año
    if fecha_actual > proximo_cumpleaños:
        proximo_cumpleaños = fecha_cumpleaños.replace(year=año_actual + 1)

    # Calcular la diferencia de tiempo hasta el próximo cumpleaños
    tiempo_faltante = proximo_cumpleaños - fecha_actual

    return tiempo_faltante

if __name__ == "__main__":
    fecha_cumpleaños = input("Ingrese su fecha de cumpleaños (dd/mm/aaaa): ")

    try:
        tiempo_faltante = calcular_tiempo_hasta_cumpleaños(fecha_cumpleaños)
        dias_faltantes = tiempo_faltante.days
        print(f"Faltan {dias_faltantes} días para su próximo cumpleaños.")
    except ValueError:
        print("Formato de fecha incorrecto. Utilice dd/mm/aaaa.")
