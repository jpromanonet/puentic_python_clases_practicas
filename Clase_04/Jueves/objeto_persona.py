# Vamos a crear una clase llamada persona
class Persona:
    # Vamos a crear un metodo __init__ como constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Vamos a crear un metodo (función) que imprima el contenido del objeto persona
    def imprimir_datos(self):
        print(f'{self.nombre}, {self.edad}')
    
    # Vamos a crear otro metodo para saber si es mayor o menor de edad
    def es_mayor(self):
        if self.edad >= 18:
            self.imprimir_datos()
            print('Es mayor de edad.')
            return True
        else:
            self.imprimir_datos()
            print("Es menor de edad.")

# Vamos a instanciar la clase Persona y crear objetos.
persona1 = Persona("Juan", 17)
persona1.es_mayor()