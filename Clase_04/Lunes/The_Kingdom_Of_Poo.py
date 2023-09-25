# Vamos a importar dos librerias para el juego
import random
import time

# Vamos a crear una clase para el juego
class JugarAventura:
    def __init__(self):
        # Creamos un diccionario de criaturas
        self.criaturas_magicas = {
            "duende":"¡Un duende aparecio y te lanzo un hechizo!",
            "hada": "Te encontraste con un hada que te concede un deseo, pero ¡Cuidado con lo que deseas!.",
            "hechicero": "Un hechiero te desafia a un duelo de magos.",
            "dragón": "Un dragón bloquea tu camino, ¿qué haras?, tene cuidado de no quemarte.",
            "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda."
        }

        # Creamos una lista con los objetos del juego
        self.objetos = ["poción mágica", "mapa", "un libro", "antorcha", "espada afilada", "mofeta", "poción multijugos", "armadura", "casco", "poción restauradora","llave","arco y flecha","galeones de oro", "sombrero"]

        # Creamos una lista con el objeto mochila
        self.mochila = ["varita mágica"]

        # Creamos una tupla con los caminos
        self.caminos = ("izquierda","derecha")
    
    def jugar(self):
        # Definir los niveles
        nivel = 1
        niveles_totales = random.randint(3,10)

        # Mensajes de inicio del juego
        print("\n")
        print("Bienvenido a la aventura en el bosque oscuro del reino de Py.")
        print("Estás en la entrada del bosque y debes tomar decisiones para avanzar por el.")
        print("Tu objetivo es encontrar la salida del bosque sin morir en el intento.")
        time.sleep(2)

        # Vamos a jugar (y no con Hugo) hasta que lleguemos al final del bosque.
        while nivel <= niveles_totales:
            print(f'Nivel {nivel} de {niveles_totales}')
            print("\n")
            # Declaramos una variable con un input para preguntar al usuario que camino elige.
            eleccion = input("¿Qué camino vas a tomar?, ¿izquierda o derecha?: ").lower()
            print("\n")
            # Creamos un condicional que llame a la función que corresponda según izquierda o derecha y sino que nos alerta que la opción elegida no es valida.
            if eleccion == "izquierda":
                # Si la función encontrar_criatura devuelve TRUE suma 1 nivel, si devuelve FALSE no suma nada.
                if self.encontrar_criatura(nivel):
                    nivel += 1
            elif eleccion == "derecha":
                self.encontrar_objeto()
            else:
                print("¡Esa elección no es valida, elegi entre izquierda y derecha, estoy seguro que perderas.")
        
        # Finaliza el juego
        print("¡Felicitaciones!, llegaste al final del bosque, sano y salvo.")
        print("Está aventura ha llegado a su fin, volve al menú principal por más aventuras.")

    def encontrar_criatura(self, nivel_jugador):
        # Tenemos que elegir de forma aleatoria una critura del diccionaro, pero solo la clave y no el valor
        criatura = random.choice(list(self.criaturas_magicas.keys()))
        # Generamos un nivel aleatorio de criatura
        nivel_criatura = random.randint(1,5)

        # Vamos a presentar el desafio
        print("\n")
        print(f'\n Te encontras a: {criatura} de nivel {nivel_criatura} con el mensaje: {self.criaturas_magicas[criatura]}')
        print("\n")
        time.sleep(2)

        # Vamos a comparar el nivel del jugador contra la criatura mágica y determinar si puede jugar o debe huir.
        if nivel_jugador >= nivel_criatura:
            # Le preguntamos al usuario si desea atacar o huir y actuamos en consecuencia.
            decision = input("\n¿Que vas a hacer? (atacar/huir): ").lower()
            if decision == "atacar":
                print(f'Has derrotado a {criatura} de nivel {nivel_criatura} y ganaste un nivel de experiencia.')
                print("\n")
                time.sleep(2)
                return True
            elif decision == "huir":
                print("Escapas del peligro y continuas tu camino pero no ganas experiencia.")
                time.sleep(2)
                return False
            else:
                print("Decisión no valida, debes elegir entre atacar o huir")
                time.sleep(2)
                return False
        else:
            print(f"El nivel de {criatura} es demasiado alto. ¡Debes huir!")
            time.sleep(2)
            print("\n.............")
            print("Lograste huir con exito y continuar tu camino")
            time.sleep(2)
            return False
        
    # Vamos a crear una función para encontrar objetos
    def encontrar_objeto(self):
        # Seleccionamos un objeto de forma aleatoria de la lista de objetos
        objeto_encontrado = random.choice(self.objetos)
        print(f'Encontraste {objeto_encontrado} en tu camino.')
        print('\n')
        time.sleep(2)
        
        # Preguntamos al jugador si desea agarrar el objeto o no.
        decision = input(f'¿Queres agarrar {objeto_encontrado}, elegi si(s) o no(n): ').lower()
        time.sleep(2)
        if decision == "si" or decision == "s":
            # lista.apped(valor) suma un elemento al final de una lista
            self.mochila.append(objeto_encontrado)
            print(f'\nAgarraste {objeto_encontrado} y lo guardaste en la mochila')
        elif decision == "no" or decision == "n":
            print(f'\nDecides dejar {objeto_encontrado} y continuar tu camino')
        else:
            print("\nDecisión no valida. Tenes que elegir que elegir entre si(s) o no(n)")
        
        # Mostramos los objetos en la lista mochila
        print(f'\nObjetos totales en tu mochila: {self.mochila}')
        time.sleep(2)

# Iniciar el juego
if __name__ == "__main__":
    jugar_aventura = JugarAventura()
    jugar_aventura.jugar()