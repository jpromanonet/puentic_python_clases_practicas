# Vamos a llamar a la libreria de números aleatorios
import random

# Vamos a crear un diccionario de criaturas
criaturas_magicas = {
    "duende": "¡Un duende aparecio y te lanzo un hechizo!",
    "bruja": "Te encontraste una bruja y te golpeo con la escoba",
    "hada": "Te encontraste con un hada que te concede un deseo, pero ¡cuidado!",
    "hechicero": "Un hechicero te desafia a un juego de adivinanzas",
    "dragón": "Un dragón bloquea tu camino, ¿Qué haras?, tene cuidado de no quemarte.",
    "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda."
}

# Creamos una lista de objetos que le jugador puede encontrar
objetos = ["poción mágica", "mapa del tesoro", "un libro", "antorcha", "espada afilada", "espada mata dragones", "alfombra mágica", "poción multijugos","baculo magico", "armadura","casco","poción restauradora","llave", "arco y flecha", "gnomo", "amuleto", "doblones de oro", "galeones", "La amiga de Valeria", "lanza"]

# Vamos a crear una lista para guardar objetos
mochila = ["Varita"]

# Vamos a crear una tupla con los caminos a elegir
caminos = ("izquierda","derecha")

# Vamos a crear una función para iniciar y jugar el juego
def jugar_aventura():

    # Definir los niveles
    nivel = 1
    niveles_totales = random.randint(3,10)

    # Mensajes de inicio del juego
    print('\n')
    print("Bienvenide a la aventura en el bosque oscuro")
    print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar.")
    print("Tu objetivo es encontrar el tesoro oculto al final del bosque. \n")

    # Jugamos hasta que lleguemos al nivel final
    while nivel <= niveles_totales:
        print(f'Nivel {nivel} de {niveles_totales}')
        eleccion = input("¿Qué camino vas a tomar?, ¿izquierda o derecha?: ").lower()

        if eleccion not in caminos:
            print("¡Esa elección no es valida!, por favor, elegir entre el camino de la derecha o la izquierda.")
        elif eleccion == "izquierda":
            if encuentro_criatura(nivel):
                nivel += 1
        else:
            encuentro_objeto()
        
    # Finaliza el juego
    print("\n")
    print("¡Felicitaciones!, llegaste al final del bosque y encontraste el tesoro. \n")
    print("Tu aventura ha llegado a su fin.")

# Vamos a crear una función para encontrarnos una criatura mágica
def encuentro_criatura(nivel_jugador):
    criatura = random.choice(list(criaturas_magicas.keys()))
    nivel_criatura = random.randint(1,5)

    print(f'\n Te encontras a: {criatura.capitalize()} de nivel {nivel_criatura} con el mensaje: {criaturas_magicas[criatura]}')

    if nivel_jugador >= nivel_criatura:
        decision = input("\n¿Qué vas a hacer? (atacar/huir): ").lower()
        if decision == "atacar":
            print(f'Has derrotado a {criatura} y ganaste 1 nivel de experiencia.')
            return True
        elif decision == "huir":
            print("Escapas del peligro y continuas tu camino.")
            return False
        else:
            print("Decisión no valida, debes elegir entre atacar o huir.")
            return False
    else:
        print("El nivel de la criatura es demasiado alto. ¡Debes huir!")
        return False

# Vamos a crear una función para encontrar objetos
def encuentro_objeto():
    objeto_encontrado = random.choice(objetos)
    print(f'Encontraste {objeto_encontrado}')

    decision = input(f'¿Queres agarrar {objeto_encontrado}? Elegi si(s) o no(n): ').lower()

    if decision == "si" or decision == "s":
        mochila.append(objeto_encontrado)
        print(f'Agarraste {objeto_encontrado} y lo guardaste en tu mochila.')
    elif decision == "no" or decision == "n":
        print(f'Decides dejar {objeto_encontrado} y continuar tu camino.')
    else:
        print("Decisión no valida. Tenes que elegir entre si(s) o no(n).")

    # Mostramos los objetos totales en la mochila
    print(f'\nObjetos totales en la mochila: {mochila}')

# Inicializar el juego
jugar_aventura()