# Declaramos una lista de numeros
numeros = [1,2,3,4,5,6,7,8,9]

# Vamos a imprimir en pantalla la lista completa
print(numeros)
print("-----------------------------")

#Vamos a imprimir solo el tercer elemento de la lista
print("El tercer numero es:", numeros[2])

# Modificamos la lista, reemplazamos el número 9 por la palabra "Python"
numeros[8] = ["Python", "PHP", "Javascript"]
print(numeros)
print(numeros[8][1])
# Esto significa que las listas son mutables y los tipos pueden ser cualquiera.