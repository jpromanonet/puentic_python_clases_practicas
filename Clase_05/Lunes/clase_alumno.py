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
    def obtener_promedio_anual(self, year):
        promedio_anual = [materia['nota'] for materia in self.materias if materia['year'] == year]
        if promedio_anual:
            return sum(promedio_anual) / len(promedio_anual)
        else:
            return 0
    
    # Creamos un metodo para obtener el promedio general
    def obtener_promedio_general(self):
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
            return "No hay materias registradas"
        
    # Metodo para materias desaprobadas
    def materias_desaprobadas(self, nota_minima):
        materias_desaprobadas = [materia['nombre'] for materia in self.materias if materia['nota'] < nota_minima]
        return materias_desaprobadas
        
# Veamos un ejemplo de uso
materias_juan = [
    {
        'nombre': "Matemática", 
        'year': 2023, 
        'nota': 10
    },
    {
        'nombre': 'Geografia',
        'year': 2022,
        'nota': 3,
    },
    {
        'nombre': 'Fisica',
        'year': 2023,
        'nota': 8.5
    }
]

# Instanciar la clase alumno
juan = Alumno("Juan", "Romano", 29, 12345678, materias_juan)

# Imprimimos en pantalla los resultados.
print('Promedio de notas en 2023:', juan.obtener_promedio_anual(2023))
print('Promedio general de notas:', juan.obtener_promedio_general())
print('Mejor materia del alumne:', juan.mejor_materia())
print('Materias desaprobadas: ', juan.materias_desaprobadas(7.0))