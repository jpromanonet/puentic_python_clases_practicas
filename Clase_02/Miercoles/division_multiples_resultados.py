# Vamos a crear una función llamada dividir
def dividir(dividendo, divisor):
    if divisor == 0:
        return 'No se puede dividir por cero.'
    else:
        resultado = dividendo / divisor
        resto = dividendo % divisor
        return resultado, resto

# Llamamos a la función con dos números
dividendo = float(input("Ingrese el dividendo: "))
divisor = float(input("Ingrese el divisor: "))
resultado, resto = dividir(dividendo, divisor)

# Mostramos los valores en pantalla
print(f'Resultado de la división: {resultado} y el resto es: {resto}.')