# Primero vamos a declarar una clase alumno
class Alumno:
    # Creamos un constructor
    def __init__(self, nombre, apellido, edad, DNI, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.DNI = DNI
        self.materias = materias
    
    # Vamos a crear un metodo para obtener el promedio anual
    def obtener_promedio_anual(self, anio):
        promedio_anual = [materia['nota'] for materia in self.materias if materia['anio'] == anio]
        if promedio_anual:
            return sum(promedio_anual) / len(promedio_anual)
        else:
            return 0
    
    # Creamos un metodo para calcular el promedio general
    def promedio_general(self):
        notas = [materia['nota'] for materia in self.materias]
        if notas:
            return sum(notas) / len(notas)
        else:
            return 0
        
    # Creamos un metodo para calcular la mejor materia
    def mejor_materia(self):
        if self.materias:
            mejor_materia = max(self.materias, key = lambda materia: materia['nota'])
            return mejor_materia['nombre']
        else:
            return 'No hay materias registradas'
    
    # Metodo para materias desaprobadas
    def materias_desaprobadas(self, nota_minima):
        materias_desaprobadas = [materia['nombre'] for materia in self.materia if materia['nota'] < nota_minima]
        return materias_desaprobadas