# Primero definimos la lista de números
numeros = [1,2,3,4,5,6,7,8,9,10]

# Declarar una variable de acumulador
acumulador = 0

# Recorrer la lista de numeros
for numero in numeros:
    if numero % 2 == 0:
        acumulador += numero
    

# Imprimir en pantalla la suma total de números pares
print("La suma total de los pares de la lista es:", acumulador)