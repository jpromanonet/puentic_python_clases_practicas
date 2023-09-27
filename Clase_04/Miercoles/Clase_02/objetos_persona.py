# Creamos una clase persona
class Persona:
    # definimos el constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # Vamos a imprimir los valores de la clase persona
    def imprimir_datos(self):
        print(f'{self.nombre}, {self.edad}')
    
    # Creamos un metodo para definir si es mayor de edad o no
    def es_mayor(self):
        if self.edad >= 18:
            self.imprimir_datos()
            print("Es mayor de edad.")
            return True
        else:
            self.imprimir_datos()
            print("Es menor de edad.")

# Vamos a instanciar la clase Persona, es decir, vamos a crear objetos.
persona1 = Persona("Juan", 29)
persona2 = Persona("Valeria", 16)
persona3 = Persona("Lucas", 28)
persona4 = Persona("Marisa", 30)
persona5 = Persona("Antonio", 54)
persona6 = Persona("Esteban", 15)
persona7 = Persona("Karen",22)

# Creamos una lista de personas
personas = [persona1,persona2,persona3,persona4,persona5,persona6,persona7]

# Recorremos la lista y nos va a devolver los resultados de los metodos de la clase Persona
for persona in personas:
    persona.es_mayor()