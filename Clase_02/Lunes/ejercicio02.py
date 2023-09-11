# Definimos una lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

# Declarar una variable para sumar los números pares
sumaPares = 0

# Primero declaramos una función que sume los números pares
def siSumaEsPar(num, sum):
    if num % 2 == 0:
        sum += num
        
    return sum

# Recorremos la lista de números
for numero in numeros:
    sumaPares = siSumaEsPar(numero, sumaPares)

# Vamos a imprimir en pantalla la suma total de números pares
print("La suma de los pares de la lista es", sumaPares)