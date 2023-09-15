# Creamos una función llamada dividir que nos retorne 2 valores
def dividir(dividendo, divisor):
    if divisor == 0:
        return "No se puede dividir por cero."
    else:
        resultado = dividendo // divisor
        resto = dividendo % divisor
        return resultado, resto

resultado, resto = dividir(780450.93,427.3)
print(resultado, resto)