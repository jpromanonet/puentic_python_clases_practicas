# Creamos una función que busque a los alumnes dentro de un diccionario con dni
def ExisteAlumno(dni_buscar):
    for alumno in lista_alumnos:
        if alumno.get("dni") == dni_buscar:
            return True
        return False

# Creo una lista de alumnoes
lista_alumnos = [
    {"nombre": "Juan", "dni": "12345678"},
    {"nombre": "Marcelo", "dni": "12345679"},
    {"nombre": "Gustavo", "dni": "12345677"},
]

# Declaramos una variable que contenga el DNI a buscar
dni = "12345678"

if ExisteAlumno(dni):
    print(f"El alumno con DNI: {dni} existe en la lista")
else:
    print(f"El alumno con DNI: {dni} no existe en la lista")