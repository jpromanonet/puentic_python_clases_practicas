# Vamos a crear una función para solicitar números al usuario
def solicitar_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un número valido.")

# Función para realizar las operaciones matemáticas
def calcular(primerNumero, segundoNumero, operacion):
    if operacion == '+':
        return primerNumero + segundoNumero
    elif operacion == '-':
        return primerNumero - segundoNumero
    elif operacion == '*':
        return primerNumero* segundoNumero
    elif operacion == '/':
        if segundoNumero != 0:
            return primerNumero / segundoNumero
        else:
            return "Error: No se puede dividir por cero."
    else:
        return "Operación no valida"
    
# Funcion principal
def main():
    primerNumero = solicitar_numero("Ingrese el primer número: ")
    segundoNumero = solicitar_numero("Ingrese el segundo número: ")
    operacion = input("Ingrese la operación (+,-,*,/): ")

    # Llamamos a la función para calcular con los inputs
    resultado = calcular(primerNumero, segundoNumero, operacion)

    # Mostramos en pantalla
    print(f'El resultado de {primerNumero} {operacion} {segundoNumero} = {resultado}')

# Invocamos nuestra función principal
if __name__ == "__main__":
    main()