# Declaramos una tupla con números de coma flotante o reales
valoresFijos = (0.25,0.5,0.75)

# Declaramos una lista con números enteros
valoresVariables = [100,100,100]

## Vamos a realizar operaciones aritmeticas con los valores variables y los fijos
valoresVariables[0] = valoresVariables[0] * valoresFijos[0]
valoresVariables[1] = valoresVariables[1] * valoresFijos[1]
valoresVariables[2] = valoresVariables[2] * valoresFijos[2]

## Imprimimos en pantalla el resultado
print(valoresVariables)