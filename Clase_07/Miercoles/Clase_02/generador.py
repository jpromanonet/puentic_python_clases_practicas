# Vamos a crear un generador
def numeros_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Uso del generador
for num in numeros_pares(100000):
    print(num)

'''
generador = numeros_pares(100)
print(next(generador)) # Se utiliza para testear que se cumplan N parametros en una operación
print(next(generador))
'''