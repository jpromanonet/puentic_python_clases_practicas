# Vamos a crear un diccionario con números de telefono
agendaDeTelefonos = {
    "Alejandro": "4444-4444",
    "Alvaro": "5555-5555",
    "Atilio": "6666-6666"
}

# Vamos a acceder a los valores del diccionario
telefonoAlejandro = agendaDeTelefonos["Alejandro"]
telefonoAlvaro = agendaDeTelefonos["Alvaro"]
telefonoAtilio = agendaDeTelefonos["Atilio"]

# Imprimimos los telefonos en pantalla
print("El telefono de Alejandro es:", telefonoAlejandro)
print("El telefono de Alvaro es:", telefonoAlvaro)
print("El telefono de Atilio es:", telefonoAtilio)

# Los diccionarios tienen funciones de ABM (en inglés CRUD), es decir: Altas, Bajas, Modificaciones
agendaDeTelefonos["Juan"] = "11-2716-9270"

print(agendaDeTelefonos)