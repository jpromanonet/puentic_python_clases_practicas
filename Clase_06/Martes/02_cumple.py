# Exportamos datetime desde python
from datetime import datetime

def calcular_tiempo_hasta_cumple(fecha_cumple):
    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Convertir la fecha de cumpleaños proporcionada por el usuario en un objete datime
    fecha_cumple = datetime.strptime(fecha_cumple, "%d/%m/%Y")

    # Calcular la fecha del próxima cumpleaños
    cumple_actual = fecha_actual.year
    proximo_cumple = fecha_cumple.replace(year=cumple_actual)

    # Verificar si el proximo cumpleaños ya ocurrio este año y si es asi, calcular para el proximo año
    if fecha_actual > proximo_cumple:
        proximo_cumple = fecha_cumple.replace(year = cumple_actual + 1)

    # Calcular la diferencia de tiempo hasta el proximo cumpleaños
    tiempo_faltante = proximo_cumple - fecha_actual

    return tiempo_faltante

if __name__ == "__main__":
    fecha_cumple = input("Ingrese su fecha de cumpleaños (dd/mm/aaaa): ")

    try:
        tiempo_faltante = calcular_tiempo_hasta_cumple(fecha_cumple)
        dias_faltantes = tiempo_faltante.days
        print(f'Faltan {dias_faltantes} días para tu próximo cumpleaños.')
    except ValueError:
        print("Formato de fecha incorrecto, Utilice dd/mm/aaaa")