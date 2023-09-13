# Definimos una lista de números
numeros = [1,2,3,4,5,6,7,8,9,10] # La suma total de los números pares es 30

# Declaramos una variables para sumar los números pares.
sumaPares = 0

# Declarar una función que sume los números pares
def siEsParSuma(num, sum):
    if num % 2 == 0:
        sum += num
    return sum

# Recorrer la lista de números
for numero in numeros: # POR CADA numero EN numeros
    sumaPares = siEsParSuma(numero, sumaPares)

# Imprimimos en pantalla la suma total de números pares
print("La suma total de los pares de la lista es:", sumaPares)