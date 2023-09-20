# Creamos una clase persona
class Persona:
    # Definimos la clase persona
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
            print("Es menor de edad")
            return False

# Vamos a instanciar la clase, es decir, vamos a crear objetos
persona1 = Persona("Juan",29)
persona2 = Persona("Franco", 20)
persona3 = Persona("Federico",29)
persona4 = Persona("Camila",26)
persona5 = Persona("Matias", 33)
persona5 = Persona("Victoria", 27)
persona6 = Persona("Jose",27)
persona7 = Persona("Axel",25)
persona8 = Persona("Carla", 40)
persona9 = Persona("Martin",37)

# Creamos una lista de personas
personas = [persona1,persona2,persona3,persona4,persona5,persona6,persona7,persona8,persona9]

for persona in personas:
    persona.es_mayor()