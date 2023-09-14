# Declaramos variables para solicitar al usuario desde la consola los números y la operación
primerNumero = float(input("Ingrese el primer número: "))
segundoNumero = float(input("Ingrese el segundo número: "))
operacion = input("Seleccionar la operación (+,/,-,*): ")

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
        print("Error: No se puede dividir por cero")
else:
    print("Operacion no valida")

# Imprimimos en pantalla utilizando f-strings
print(f'El resultado de {primerNumero} {operacion} {segundoNumero} es igual a {resultado}')
    