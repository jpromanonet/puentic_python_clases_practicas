# Vamos a crear un generador
def numeros_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Vamos a usar el generador
for num in numeros_pares(100000):
    print(num)