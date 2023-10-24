# Vamos a crear un decorador
def mi_decorador(func):
    def envoltura():
        print("Antes de llamar a la función.")
        func()
        print("Despues de llamar a la función")
    return envoltura

@mi_decorador
def mi_funcion():
    print("Dentro de la función.")

mi_funcion()