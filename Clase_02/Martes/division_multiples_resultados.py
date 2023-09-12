# Vamos a crear una función llamada dividir
def dividir(primerNumero, segundoNumero):
    if primerNumero == 0:
        return "No se puede dividir por cero"
    elif segundoNumero == 0:
        return "No se puede dividir por cero"
    else:
        resultadoDivision = primerNumero / segundoNumero
        resto = primerNumero % segundoNumero
        return resultadoDivision, resto

# Llamamos a la función con dos números
primerNumero = float(input("Ingrese el primer numero: "))
segundoNumero = float(input("Ingrese el segundo número: "))
resultado, resto = dividir(primerNumero, segundoNumero)

# Mostramos los valores resultantes en pantalla
print(f"Resultado de la división: {resultado} y el resto es: {resto}")