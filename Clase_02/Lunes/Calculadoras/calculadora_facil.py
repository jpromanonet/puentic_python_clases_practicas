# Solicitar al usuario dos números y una operación matemática
primerNumero = float(input("Ingrese el primer número: "))
segundoNumero = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación matemática (+,-,*,/): ")

# Realizar la operación y mostrar el resultado
if operacion == '+':
    resultado = primerNumero + segundoNumero
elif operacion == '-':
    resultado = primerNumero - segundoNumero
elif operacion == '*':
    resultado = primerNumero * segundoNumero
elif operacion == '/':
    if segundoNumero != 0:
        resultado = primerNumero / segundoNumero
    else:
        resultado = "Error: No se puede dividir por cero."
else:
    resultado = "Operación no valida."

# Mostrar el resultado utilizando f-strings
print(f"Resultado: {resultado}")
