# Creamos una clase persona
class Persona:
    # definimos la clase persona
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
            print("Es mayor de edad")
            return True
        else:
            self.imprimir_datos()
            print("Es menor de edad")
            return False

# Vamos a instanciar la clase Persona, es decir, vamos a crear objetos
persona1 = Persona("Juan", 29)
persona2 = Persona("Pamela", 34)
persona3 = Persona("Agustina", 17)
persona4 = Persona("Maite", 31)
persona5 = Persona("Christian", 45)

# Creamos una lista de personas
personas = [persona1, persona2, persona3, persona4, persona5]

# Recorremos la lista y nos va a devolver los resultados de los metodos de la clase Persona.
for persona in personas:
    persona.es_mayor()