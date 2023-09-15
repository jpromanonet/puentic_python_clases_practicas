# Primero definimos la lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

# Declarar una variable de acumulador
acumulador = 0

# Declarar una funcion que sume los números pares
def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Recorrer la lista de numeros
for numero in numeros:
    if esPar(numero):
        acumulador += numero

# Imprimir en pantalla la suma total de números pares
print("La suma total de los pares de la lista es:", acumulador)