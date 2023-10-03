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
    
# Vamos a declarar una clase Materia
class Materia:
    def __init__(self, nombre, anio, nota):
        self.nombre = nombre
        self.anio = anio
        self.nota = nota

# Declaramos una clase llamada Academico
class Academico:
    def __init__(self, nombre_institucion, alumnos):
        self.nombre_institucion = nombre_institucion
        self.alumnos = alumnos
    
    # Vamos a crear un metodo de promedio general
    def promedio_general(self):
        # Vamos a definir la cantidad de materias y notas en 2 variables
        total_notas = 0
        total_materias = 0
        # Recorremos todas las materias y sus notas para calcular el promedio
        for alumno in self.alumnos:
            for materia in alumno.materias:
                total_notas += materia.nota
                total_materias += 1
        if total_materias > 0:
            return total_notas / total_materias
        else:
            return 0
        
    # Creamos un metodo de alumnos graduados
    def alumnos_graduados(self):
        alumnos_graduados = []
        # Recorremos a los alumnos
        for alumno in self.alumnos:
            materias_aprobadas = all(materia.nota >= 7.0 for materia in alumno.materias)
            if materias_aprobadas:
                alumnos_graduados.append(alumno)
        return alumnos_graduados
    
# Ejemplo de uso

## Creamos 2 variables con las materias, año y notas de cada una, vamos a tener 2 objetos de la clase Materia en dos listas
materias_juan = [Materia("Matematica", 2023, 8.5), Materia("Historia", 2022, 7.0)]
materias_pedro = [Materia("Matematica", 2023, 7.0), Materia("Historia", 2022, 8.5)]

## Llamamos a la clase Alumno del ejercicio anterior para utilizar los metodos de la clase
juan = Alumno("Juan", "Romano", 18, 12345678, materias_juan)
pedro = Alumno("Pedro", "Gomez", 19, 87654321, materias_pedro)

## Asignamos ambos objetos alumno a dos variables que sean objetos de la clase Academico
academico = Academico("Universidad Tecnologica Nacional", [juan, pedro])
academico2 = Academico("Universidad Nacional de Cordoba", [juan, pedro])

# Vamos a imprimir en pantalla
print("Promedio general de todas las materias de todos los alumnos:", academico.promedio_general(), academico2.promedio_general())
print("\nAlumnos graduados:")
for alumno in academico.alumnos_graduados():
    print(alumno.nombre, alumno.apellido, academico.nombre_institucion)