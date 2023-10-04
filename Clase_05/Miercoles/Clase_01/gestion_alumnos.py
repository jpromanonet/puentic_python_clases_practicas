# Declaramos una clase alummno
class Alumno:
    # Creamos el constructor
    def __init__(self, nombre, apellido, edad, DNI, materias):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.DNI = DNI
        self.materias = materias

    # Creamos un metodo para obtener el promedio anual
    def obtener_promedio_anual(self, anio):
        promedio_anual = [materia['nota'] for materia in self.materias if materia['anio'] == anio]
        if promedio_anual:
            return sum(promedio_anual) / len(promedio_anual)
        else: 
            return 0
    
    # Creamos un metodo para obtener promedios generales
    def obtener_promedio_general(self):
        notas = [materia['nota'] for materia in self.materias]
        if notas:
            return sum(notas) / len(notas)
        else:
            return 0
    
    # Creamos un metodo para calcular la mejor materia
    def mejor_materia(self):
        if self.materias:
            # Aplicamos nuestra primera función lambda
            mejor_materia = max(self.materias, key = lambda materia: materia['nota'])
            return mejor_materia['nombre']
        else:
            return "No hay materias registradas"
    
    # Metodo de materias desaprobadas
    def materias_desaprobadas(self, nota_minima):
        materias_desaprobadas = [materia['nombre'] for materia in self.materias if materia['nota'] < nota_minima]
        return materias_desaprobadas
    
# Creamos una clase para las materias
class Materia:
    def __init__(self, nombre, anio, nota):
        self.nombre = nombre
        self.anio = anio
        self.nota = nota

# Declaramos una clase llamada Academico
class Academico:
    # Creamos un constructor para la clase
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
                # Aca llamamos a la clase Alumno y recoreemos la lista de materias del argumento materias que consume el atributo del constructor de la clase Alumno, esto es una forma de "Anidar clases"
            for materia in alumno.materias:
                total_notas = materia.nota
                total_materias += 1
        if total_materias > 0:
            return total_notas / total_materias
        else:
            return 0
        
    # Creamos un metodo de alumno graduados
    def alumnos_graduados(self):
        alumnos_graduados = []
        # Recorremos la lista de alumnos
        for alumno in self.alumnos:
            materias_aprobadas = all(materia.nota >= 4.0 for materia in alumno.materias)
            if materias_aprobadas:
                alumnos_graduados.append(alumno)
        return alumnos_graduados

# Ejemplo de uso

## Creamos 2 variables con las materias, años, notas de cada una y vamos a tener 2 objetos de clase Materia en dos listas

materias_juan = [Materia("Matemática", 2023, 8.5), Materia("Historia", 2022, 7.0)]
materias_pedro = [Materia("Matemática", 2023, 6.0), Materia("Historia", 2022, 9.0)]

## Llamamos a la clase Alumno y utilizamos sus metodos.
juan = Alumno("Juan", "Apellido", 18, 12345678, materias_juan)
pedro = Alumno("Pedro", "Apellido", 18, 12345679, materias_pedro)

## Llamamos a la clase Academico
academico = Academico("- Universidad de Buenos Aires", [juan, pedro])

# Vamor a imprimir en pantalla
print("Promedio general de todas las materias de los alumnos:", academico.promedio_general())
print("\nAlumnos graduados:")
for alumno in academico.alumnos_graduados():
    print(f'{alumno.nombre} {alumno.apellido} - {academico.nombre_institucion}')
    print('\n')