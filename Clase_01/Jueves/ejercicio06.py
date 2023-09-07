# Declaramos una tupla con números de coma flotante mejor conocidos como decimales
valoresFijos = (0.25,0.5,0.75)

# Declaramos una lista de valores variables
valoresVariables = [100,100,100]
print(valoresVariables)

## Realizamos operaciones aritmeticas con los valores variables y los fijos
valoresVariables[0] = valoresVariables[0] * valoresFijos[0]
valoresVariables[1] = valoresVariables[1] * valoresFijos[1]
valoresVariables[2] = valoresVariables[2] * valoresFijos[2]

## Imprimirlo en pantalla
print(valoresVariables)