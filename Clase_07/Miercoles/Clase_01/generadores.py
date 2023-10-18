# Generador
def numeros_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i # Reemplazas el return con yield

# ¿Cómo usamos el generador?
'''
for num in numeros_pares(1000000):
    print(num)
'''

generador = numeros_pares(100)

print(next(generador))
print(next(generador))
print(next(generador))