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
            eleccion = input('¿Qué camino vas a tomar para avanzar?, elegi entre izquierda o derecha: ').lower()
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

    # Creamos un metodo para encontrar criatura cada vez que elegimos la izquierda
    def encontrar_criatura(self, nivel_jugador):
        # Tenemos que elegir de forma aleatoria una criatura del diccionario
        criatura = random.choice(list(self.criaturas_magicas.keys()))
        # Generamos un nivel aleatorio para nuestra criatura mágica
        nivel_criatura = random.randint(1,10)

        # Vamos a presentar el desafio
        print("\n")
        print(f'\nTe encontras a: {criatura} de nivel {nivel_criatura} con el mensaje: {self.criaturas_magicas[criatura]}')
        print('\n')
        time.sleep(2)

        # Vamos a comprar el nivel del jugador contra la criatura mágica y determinar si puede jugar o debe huir.
        if nivel_jugador >= nivel_criatura:
            # Le preguntamos al usuario si desea atacar o huir
            decision = input("\n¿Qué vas a hacer? (atacar/huir): ").lower()
            print('\n')
            if decision == "atacar":
                print(f'Has derrotado a {criatura} de nivel {nivel_criatura} y ganaste un nivel de experiencia.')
                print('\n')
                time.sleep(2)
                return True
            elif decision == "huir":
                print("Escapas del peligro y continuas tu camino pero no ganas experiencia.")
                time.sleep(2)
                return False
            else:
                print("Decisión no valida, tenes que elegir entre atacar o huir.")
                time.sleep(2)
                return False
        else:
            print(f'El nivel de {criatura} es demasiado alto. ¡Debes huir!')
            time.sleep(2)
            print("\n______________________________________________________________________________________\n")
            print("Lograste huir con exito y continuar tu camino.")
            time.sleep(1)
            return False
        
    # Vamos a crear una función para encontrar objetos
    def encontrar_objeto(self):
        # Seleccionamos un objeto de forma aleatoria de la lista de objetos.
        objeto_encontrado = random.choice(self.objetos)
        print(f'Encontraste {objeto_encontrado} en tu camino.')
        print('\n')
        time.sleep(2)

        # Preguntamos al jugador si desea agarrar el objeto o no.
        decision = input(f'¿Queres agarrar {objeto_encontrado}, elegi si(s) o no(n): ').lower()
        time.sleep(1)
        if decision == "si" or decision == "s":
            # lista.append(valor) suma un elemento al final de una lista
            self.mochila.append(objeto_encontrado)
            print(f'\nAgarraste {objeto_encontrado} y lo guardaste en tu mochila')
        elif decision == "no" or decision == "n":
            print(f'\nDecides dejar {objeto_encontrado} y continuar tu camino')
        else:
            print('\nDecisión no valida, tenes que elegir entre si(s) o no(n).')
        
        # Mostramos los objetos en la mochila
        print(f'\nObjetos totales en tu mochila: {self.mochila}')
        time.sleep(2)

# Iniciar el juego
if __name__ == "__main__":
    jugar_aventura = JugarAventura()
    jugar_aventura.jugar()