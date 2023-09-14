# Definimos una lista de números
numeros = [1,2,3,4,5,6,7,8,9,10] # Suma de pares da 30

# Declarar una variable de acumulador
acumuladorDePares = 0

# Declarar una función que sume los números pares
def siEsParSuma(num, sum):
    if num % 2 == 0:
        sum += num
    return sum

# Recorrer la lista de números
for num in numeros:
    acumuladorDePares = siEsParSuma(num, acumuladorDePares)

# Imprimir en pantalla la suma total de números pares
print("La suma total de los pares de la lista es:", acumuladorDePares)