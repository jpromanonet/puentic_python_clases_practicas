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
        materias_desaprobadas = [materia['nombre'] for materia in self.materias if materia['nota'] < nota_minima]
        return materias_desaprobadas
    
# Declarar la clase materia
class Materia:
    def __init__(self, nombre, anio, nota):
        self.nombre = nombre
        self.anio = anio
        self.nota = nota

# Declaramos la clase Academico
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
        # Declarar una lista vacia de alumnos graduados
        alumnos_graduados = []
        # Recorremos a los alumnos
        for alumno in self.alumnos:
            materias_aprobadas = all(materia.nota >= 4.0 for materia in alumno.materias)
            if materias_aprobadas:
                alumnos_graduados.append(alumno)
        return alumnos_graduados
    
# Ejemplo de uso

# Creamos 2 variables con las materias, año y notas de cada una, vamos a tener 2 objetos de la clase materia en dos listas.
materias_juan = [Materia("Matemática", 2023, 8.5), Materia("Historia", 2022, 6.0)]
materias_pedro = [Materia("Matemática", 2023, 6.5), Materia("Historia", 2022, 8.0)]

# Llamamos a la clase Alumno para utilizar sus metodos
juan = Alumno("Juan", "Romano", 18, 12345678, materias_juan)
pedro = Alumno("Pedro", "Romano", 18, 12345679, materias_pedro)

# Asignar ambos objetos alumno a una variable que sea objeto de la clase academico
academico = Academico("Universidad Tecnologica Nacional", [juan, pedro])

# Vamos a imprimir en pantalla
""" print('Promedio de notas de alumnos 2023:', pedro.obtener_promedio_anual(2023))
print('Promedio general de notas:', pedro.promedio_general())
print('Mejores materias de los alumnos:', pedro.mejor_materia())
print('Materias desaprobadas:', pedro.materias_desaprobadas(7.0)) """
print('\n--------------------------------------------------------------')
print("Promedio general de todas las materias de todos los alumnos:", academico.promedio_general())
print("\nAlumnos graduados:")
for alumno in academico.alumnos_graduados():
    print(f'{alumno.nombre} {alumno.apellido} -  {academico.nombre_institucion}')