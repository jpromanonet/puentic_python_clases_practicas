# Primero vamos a declarar una clase alumno
class Alumno:
    # Creamos el constructor
    def __init__(self, nombre, apellido, edad, DNI, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.DNI = DNI
        self.materias = materias

    # Vamos a crear un metodo para obtener el promedio anual
    def obtener_promedio_anual(self, anio):
        promedio_anual = [materia['anio'] for materia in self.materias if materia['anio'] == anio]
        # Calculamos el promedio anual
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
    
    # Vamos a crear un metodo para calcular cual es la mejor materia
    def mejor_materia(self):
        if self.materias:
            mejor_materia = max(self.materias, key = lambda materia: materia['nota'])
            return mejor_materia['nombre']
        else:
            return "No hay materias registradas."
    
    # Creamos un metodo para materias desaprobadas
    def materias_desaprobadas(self, nota_minima):
        materias_desaprobadas = [materia['nombre'] for materia in self.materias if materia['nota'] < nota_minima]
        return materias_desaprobadas

# Vamos a crear una clase Materia
class Materia:
    def __init__(self, nombre, anio, nota):
        self.nombre = nombre
        self.anio = anio
        self.nota = nota

# Vamos a crear una clase Academico
class Academico:
    # Creamos el metodo constructor
    def __init__(self, nombre_institucion, alumnos):
        self.nombre_institucion = nombre_institucion
        self.alumnos = alumnos
    
    # Creamos un metodo de promedio general
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
        # Recorremos a la lista de alumnos
        for alumno in self.alumnos:
            materias_aprobadas = all(materia.nota >= 4.0 for materia in alumno.materias)
            if materias_aprobadas:
                alumnos_graduados.append(alumno)
        return alumnos_graduados

# Ejemplos de uso

## Creamos 2 variables con las materias, años y notas de cada materia, vamos a tener 2 objetos de la clase Materia en 2 listas
materias_juan = [Materia("Matemática", 2023, 8.5), Materia("Historia", 2022, 7.0)]
materias_pedro = [Materia("Matemática", 2023, 9.0), Materia("Historia", 2022, 9.0)]

## Llamamos a la clase alumno para utilizar sus metodos
juan = Alumno("Juan", "Romano", 29, 12345678, materias_juan)
pedro = Alumno("Pedro", "Romano", 29, 12345679, materias_pedro)

## Asignamos ambos objetos alumno a dos variables que sean objetos de la clase Academico
academico = Academico("Universidad de Buenos Aires", [juan, pedro])

# Vamos a imprimir en pantalla
print('Promedio general de todas las materias de todos los alumnos:', academico.promedio_general())

# Imprimimos los alumnos graduados
print("\nAlumnos Graduados:")
for alumno in academico.alumnos_graduados():
    print(alumno.nombre, alumno.apellido, academico.nombre_institucion)