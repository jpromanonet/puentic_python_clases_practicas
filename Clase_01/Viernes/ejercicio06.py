# Vamos a crear una tupla de valores fijos

## snake_case = es una forma de declarar variables utilizando guiones para separar palabras

## lowerCamelCase = donde sin espacios, separamos las palabras usando la primera letra en mayuscula.

## Buena practicas = variables con nombre significativo, NADA PERO NADA de "a1" o "a" o peor "1", o peor "uno"

valoresFijos = (0.25, 0.5, 0.75)

# Declaramos una lista en base 100
valoresVariables = [100,100,100]
print(valoresVariables)

## Multiplicamos los valores de la lista por los valores de la tupla y reemplazamos los indices de la lista.

valoresVariables[0] = valoresFijos[0] * valoresVariables[0]
valoresVariables[1] = valoresFijos[1] * valoresVariables[1]
valoresVariables[2] = valoresFijos[2] * valoresVariables[2]

## Imprimimos la lista en pantalla
print(valoresVariables)