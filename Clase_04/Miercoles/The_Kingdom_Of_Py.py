# Vamos a importar dos librerias para el juego
import random
import time

# Vamos a crear una clase para el juego
class JugarAventura:
    # Vamos a crear el constructor
    def __init__(self):
        # Creamos un diccionario de criaturas mágicas
        self.criaturas_magicas = {
            "duende":"¡Un duende aparecio y te lanzo un hechizo!",
            "hada":"Te encontraste con un hada que te concede un deseo, pero ¡Cuidado con lo que deseas!",
            "hechicero": "Un hechicero te desafia a un duelo de magos.",
            "dragón": "Un dragón bloquea tu camino, tene cuidado de no quemarte.",
            "unicornio":"Un majestuoso unicornio aparece y te ofrece su ayuda."
        }

        # Creamos una lista con los objetos del juego
        self.objetos = ["poción mágica", "mapa", "libro", "antorcha", "espada", "poción multijugos", "armadura", "casco", "poción restauradora", "llave", "arco y flecha", "galeones", "sombrero", "diamantes", "Gnomo", "gato", "perro"]

        # Vamos a crear una lista para la mochila donde guardamos objetos
        self.mochila = ["varita mágica"]

        # Tenemos que definir los caminos
        self.caminos = ("izquierda", "derecha")

    # Creamos un metodo para JUGAR al juego
    def jugar(self):
        # Vamos a definir el nivel de inicio y los niveles posibles hasta finalizarlo
        nivel = 1
        niveles_totales = random.randint(3,11)

        # Mensajes de inicio del juego
        print("\n")
        print("Bienvenido a la aventura en el bosque oscuro del reino de Py.")
        print("Estás en la entrada del bosque y debes tomar decisiones para avanzar por el.")
        print("Tu objetivo es encontrar la salidad del bosque sin morir en el intento.")
        time.sleep(2)

        # Vamos a jugar (y no con Hugo) hasta que lleguemos al final del bosque.
        while nivel <= niveles_totales:
            print(f'Nivel {nivel} de {niveles_totales}')
            print('\n')
            # Declaramos una variable con un input para preguntar al usuario que camino elige.
            eleccion = input('¿Qué camino vas a tomar para avanzar?, elegi entre izquierda o derecha: ')
            print('\n')
            # Creamos un condicional que llame a la función que corresponda según izquierda o derecha y sino que nos alerte de que no es una opción valida.
            if eleccion == "izquierda":
                # Si la función encontrar_criatura devuelve TRUE suma 1 nivel y sino no suma nada.
                if self.encontrar_criatura(nivel):
                    nivel += 1
            elif eleccion == "derecha":
                self.encontrar_objeto()
            else:
                print("¡Esa opción no es valida, elegi entre izquierda o derecha, estos seguro que perderas.")

        # Finalizar el juego
        print("Felicitaciones! llegaste al final del bosque, sano y salvo.")
        print("Esta aventura ha llegado a su fin, volve al menú principal por más aventuras.")

    