# Solicitar al usuario dos números y una operación matematica
primerNumero = float(input("Ingrese el primer número: "))
segundoNumero = float(input("Ingrese el segundo número: "))
operacion = input("Ingrese la operación matemática (+,-,/,*): ")

# Realizar las operaciones y mostrar el resultado
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
        print("Error: No se puede dividir por cero.")
else:
    print("Operación no valida")

# Mostramos el resultado en pantalla usando f-strings
print(f"Resultado: {resultado}")