def ExisteAlumno(dni_buscar):
    for alumno in lista_alumnos:
        if alumno.get("dni") == dni_buscar:
            return True
    return False

# Ejemplo de uso
lista_alumnos = [
    {"nombre": "Juan", "dni": "12345678"},
    {"nombre": "María", "dni": "87654321"},
    {"nombre": "Pedro", "dni": "55555555"},
]

dni_buscar = "12345678"
if ExisteAlumno(dni_buscar):
    print(f"El alumno con DNI {dni_buscar} existe en la lista.")
else:
    print(f"El alumno con DNI {dni_buscar} no existe en la lista.")
