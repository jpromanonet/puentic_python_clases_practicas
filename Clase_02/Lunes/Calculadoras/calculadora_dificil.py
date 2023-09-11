# Vamos a crear una función para solicitar un número al usuario:
def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número valido.")

# Función para realizar la operación matemática
def calcular(primerNumero, segundoNumero, operacion):
    if operacion == '+':
        return primerNumero + segundoNumero
    elif operacion == '-':
        return primerNumero - segundoNumero
    elif operacion == '*':
        return primerNumero * segundoNumero
    elif operacion == '/':
        if segundoNumero != 0:
            return primerNumero / segundoNumero
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación no valida."

# Función principal
def main():
    primerNumero = solicitar_numero("Ingrese el primer número: ")
    segundoNumero = solicitar_numero("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación matemática (+,-,/,*): ")

    # Llamamos a la función para calcular los inputs
    resultado = calcular(primerNumero, segundoNumero, operacion)

    # Imprimimos los resultados en pantalla
    print(f"Resultado: {resultado}")

# Vamos a ejecutar nuestra función principal cuando ejecutemos el script
if __name__ == "__main__":
    main()