import random

# Diccionario de criaturas mágicas en el bosque
criaturas_magicas = {
    "duende": "¡Un duende apareció y te lanzó un hechizo!",
    "bruja": "Te encontraste una bruja y te golpeo con su escoba",
    "hada": "Te encontraste con un hada que te concedió un deseo",
    "hechicero": "Un hechicero te desafia a un juego de adivinanzas",
    "dragón": "Un dragón bloquea tu camino. ¿Qué harás?",
    "unicornio": "Un majestuoso unicornio aparece y te ofrece su ayuda"
}

# Creamos una lista de objetos que el jugador puede encontrar
objetos = ["poción mágica", "mapa del tesoro", "espada afilada", "antorcha", "alfombra voladora", "poción multijugos", "varita", "brujula encantada"]

# Inventario del jugador
mochila = ["varita"]

# Tupla de caminos posibles
caminos = ("izquierda", "derecha")

# Creamos una función para iniciar el juego
def jugar_aventura():

    # Nivel actual de jugador
    nivel = 1
    niveles_totales = random.randint(3,10)

    print("Bienvenide a la Aventura en el Bosque Oscuro")
    print("Estás en la entrada del bosque. Debes tomar decisiones para avanzar")
    print("Tu objetivo es encontrar el tesoro oculto al final del bosque.\n")

    while nivel <= niveles_totales:
        print(f"Nivel {nivel} de {niveles_totales}")
        eleccion = input("¿Qué camino vas a tomar?, ¿izquierda o derecha? ").lower()

        if eleccion not in caminos:
            print("¡Esa no es una elección valida!, elegi entre el camino de la derecha o la izquierda")
        else:
            if eleccion == "izquierda":
                encuentro_criatura(nivel)
            else:
                encontrar_objeto()

        nivel += 1

    print("¡Felicidades! Has llegado al final del bosque y encontrado el tesoro.")
    print("Tu aventura ha llegado a su fin.")

# Función para el encuentro con una criatura mágica
def encuentro_criatura(nivel_jugador):
    criatura = random.choice(list(criaturas_magicas.keys()))
    nivel_criatura = random.randint(1,9)

    print(f"\n¡{criatura.capitalize()} de nivel {nivel_criatura}!")
    
    if nivel_jugador >= nivel_criatura:
        decision = input("¿Qué vas a hacer? (atacar/huir): ").lower()
        if decision == "atacar":
            print(f'Has derrotado a {criatura} y ganaste {nivel_criatura} de experiencia.')
        elif decision == "huir":
            print("Escapas del peligro y continuas tu camino.")
        else:
            print("Decisión no valida, debes elegir entre atacar o huir.")
    else:
        print("El nivel de la criatura es demasiado alto. ¡Debes huir!.")

# Vamos a crear una función para encontrar un objeto
def encontrar_objeto():
    objeto_encontrado = random.choice(objetos)
    print(f'Encontraste {objeto_encontrado}')

    decision = input("¿Deseas agarrarlo? (si/no): ").lower()

    if decision == "si" or decision == "s":
        mochila.append(objeto_encontrado)
        print(f'Agarraste {objeto_encontrado} y lo guardaste en tu mochila.')
    elif decision == "no" or decision == "n":
        print("Decides dejar el objeto y continuar tu camino")
    else:
        print("Decisión no válida. Elige si(s) o no(n)")
    
    # Nos muestra la mochila al finalizar
    print(f'\nObjetos totales en tu mochila: {mochila}.')

# Iniciar
jugar_aventura()