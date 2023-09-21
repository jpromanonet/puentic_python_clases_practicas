# Llamamos a la librera random
import random

# Vamos a crear un diccionario de criaturas mágicas
criaturas_magicas = {
    "duende": "¡Un duende aparecio y te lanzo un hechizo!",
    "hada": "Te encontraste con un hada que te concede un deseo, pero ¡Cuidado con lo que deseas!",
    "hechicero":"Un hechicero te desafia a un juego de adivinanzas.",
    "dragón":"Un dragón bloquea tu camino, ¿Qué haras?, tene cuidado de no quemarte.",
    "unicornio":"Un majestuoso unicornio aparece y te ofrece su ayuda."
}

# Creamos una lista con los objetos del juego
objetos = ["poción mágica","mapa del tesoro", "un libro","antorcha", "espada afilada", "mofeta", "poción multijugos","armadura","casco","poción restauradora","llave","arco y flecha", "gnomo", "amuleto", "galeones", "horrocrux", "sombrero"]

# Creamos una lista para la mochila donde vamos a guardar los objetos
mochila = ["varita mágica"]

# Creamos una tupla de caminos
caminos = ("izquierda", "derecha")

# Vamos a crear una función para iniciar y jugar el juego
def jugar_aventura():

    # Definir los niveles
    nivel = 1
    niveles_totales = random.randint(3,10)

    # Mensajes de inicio del juego
    print("\n")
    print("Bienvenide a la aventura en el bosque oscuro del reino de Py.")
    print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar.")
    print("Tu objetivo es encontrar la salida del bosque sin morir en el intento.")

    # Vamos a jugar (y no con Hugo) hasta que lleguemos al nivel final.
    while nivel <= niveles_totales:
        print(f'Nivel {nivel} de {niveles_totales}')
        # Declaramos una variable con un input para preguntar al usuario que camino elige
        eleccion = input("¿Qué camino vas a tomar?, ¿izquierda o derecha?: ").lower()
        # Creamos un condiciónal que llame a la función que corresponda segun izquierda o derecha y sino que nos diga que la opción elegida no es valida.
        if eleccion not in caminos:
            print("¡Esa elección no es valida!, elegi bien entre izquierda y derecha, estoy seguro que perderas.")
        elif eleccion == "izquierda":
            # Si la función criatura es TRUE suma 1 nivel, si devuelve FALSE no sumes nada.
            if encontrar_criatura(nivel):
                nivel += 1
        else:
            encontrar_objeto()

    # Finaliza el juego
    print("\n")
    print("¡Felicitaciones!, llegaste al final del bosque y encontraste el tesoro.")
    print("Está aventura ha llegado a su fin, volve al menú principal por más aventuras.")

# Vamos a crear una función para encontrarnos una criatura mágica.
def encontrar_criatura(nivel_jugador):
    criatura = random.choice(list(criaturas_magicas.keys()))
    nivel_criatura = random.randint(1,9)

    # Vamos a presentar el desafio
    print(f'\n Te encontras a: {criatura} de nivel {nivel_criatura} con el mensaje: {criaturas_magicas[criatura]}.')

    # Vamos a comparar el nivel del jugador contra la criatura y determinar si puede jugar o huir
    if nivel_jugador >= nivel_criatura:
        # Le preguntamos al usuario si desea atacar o huir y actuamos en consecuencia.  
        decision = input("\n¿Qué vas hacer? (atacar/huir): ").lower()
        if decision == "atacar":
            print(f'Has derrotado a {criatura} y ganaste 1 nivel de experiencia.')
            return True
        elif decision == "huir":
            print("Escapas del peligro y continuas tu camino pero no ganas experiencia.")
            return False
        else:
            print("Decisión no valida, debes elegir entre atacar o huir.")
    else:
        print("El nivel de la criatura es demasiado alto. ¡Debes huir!")
        return False    

# Vamos a crear una función para encontrar objetos
def encontrar_objeto():
    # Seleccionamos un objeto de forma aleatoria de la lista de objetos.
    objeto_encontrado = random.choice(objetos)
    print(f'Encontraste {objeto_encontrado} en tu camino.')

    # Preguntamos al usuario si desea agarrarlo o dejarlo.
    decision = input(f'¿Queres agarrar {objeto_encontrado}?, elegi si(s) o no(n): ').lower()
    if decision == "si" or decision == "s":
        # .append(valor) suma un elemento N al final de una lista.
        mochila.append(objeto_encontrado)
        print(f'Agarraste {objeto_encontrado} y lo guardaste en tu mochila.')
    elif decision == "no" or decision == "n":
        print(f'Decides dejar {objeto_encontrado} y continuar tu camino.')
    else:
        print("Decisión no valida. Tenes que elegir entre si(s) o no(n)")
    
    # Mostramos los objetos en la lista mochila
    print(f'\nObjetos totales en tu mochila: {mochila}')

# Iniciamos el juego.
jugar_aventura()