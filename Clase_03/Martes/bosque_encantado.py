# Llamamos una libreria para numeros aleatorios
import random

# Definimos un diccionario de criaturas
criaturas_magicas = {
    "duende": "¡Un duende aparecio y te lanzo un hechizo!",
    "bruja":"Te encontraste una bruja y te golpeo con la escoba",
    "hada":"Te encontraste con un hada que te concedio un deseo.",
    "hechicero": "Un hechicero te desafia a un juego de adivinanzas",
    "dragón": "Un dragón bloquea tu camino. ¿Qué haras?",
    "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda"
}

# Creamos una lista de objetos que el jugador puede encontrar
objetos = ["poción mágica", "mapa del tesoro", "espada afilada", "antorcha", "alfombra voladora", "poción multijugos", "brujula encantada", "capa de invisibilidad", "varita", "martillo", "llave", "poción restauradora", "arco y flecha", "gnomo", "comida", "galeones"]

# Creamos una lista con la mochila
mochila = ["varita"]

# Creamos una tupla de caminos posibles
caminos = ("izquierda", "derecha")

# Creamos una función para iniciar el juego
def jugar_aventura():

    # Definir los niveles
    nivel = 1
    niveles_totales = random.randint(3,10)

    # Mensajes de inicio del juego
    print("Bienvenide a la Aventura en el Bosque Oscuro")
    print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar")
    print("Tu objetivo es encontrar el tesoro oculto al final del bosque. \n")

    while nivel <= niveles_totales:
        print(f"Nivel {nivel} de {niveles_totales}")
        eleccion = input("¿Qué camino vas a tomar?, ¿izquierda o derecha?: ").lower()

        if eleccion not in caminos:
            print("¡Esa no es una elección valida!, elegi entre el camino de la derecha o la izquierda")
        else:
            if eleccion == "derecha":
                encontrar_objeto()
            else:
                encuentro_criatura(nivel)
                nivel += 1
    
    print("\n")
    print("¡Felicitaciones! llegaste al final del bosque y encontraste el tesoro.\n")
    print("Tu aventura ha llegado a su fin.")

# Función para el encuentro con una criatura mágica
def encuentro_criatura(nivel_jugador):
    criatura = random.choice(list(criaturas_magicas.keys()))
    nivel_criatura = random.randint(1,9)

    print(f'\nTe encontras a: {criatura.capitalize()} de nivel {nivel_criatura}')

    if nivel_jugador >= nivel_criatura:
        decision = input("¿Qué vas a hacer? (atacar/huir): ").lower()
        if decision == "atacar":
            print(f"Has derrotado a {criatura} y ganaste {nivel_criatura} de experiencia.")
        elif decision == "huir":
            print("Escapas del peligro y continuas tu camino.")
            nivel_jugador -= 1
        else:
            print("Decisión no valida, debes elegir entre atacar o huir.")
    else: 
        print("El nivel de la criatura es demasiado alto. ¡Debes huir!")

# Vamos a crear una función para encontrar un objeto
def encontrar_objeto():
    objeto_encontrado = random.choice(objetos)
    print(f'Encontraste {objeto_encontrado}')

    decision = input(f'¿Queres agarrar {objeto_encontrado}? Elegi si(s) o no(n): ').lower()

    if decision == "si" or "s":
        mochila.append(objeto_encontrado)
        print(f'Agarraste {objeto_encontrado} y lo guardaste en tu mochila.')
    elif decision == "no" or "n":
        print("Decides dejar el objeto y continuar tu camino.")
    else:
        print("Decisión no valida. Tenes que elegir entre si(s) o no(n).")

    # Nos muestra la mochila al finalizar
    print(f"\nObjetos totales en tu mochila: {mochila}")

# Iniciar juego
jugar_aventura()