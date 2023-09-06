# Vamos a crear un diccionario con números de telefono
agendaDeTelefonos = {
    "Alejandra": "4444-4444",
    "Alvaro": "5555-5555",
    "Atilio": "6666-6666"
}

print(agendaDeTelefonos)

# Vamos a acceder a los valores del diccionario
telefonoAlejandra = agendaDeTelefonos["Alejandra"]
telefonoAlvaro = agendaDeTelefonos["Alvaro"]
telefonoAtilio = agendaDeTelefonos["Atilio"]

# Vamos a imprimir en pantalla los telefonos
print("El telefono de Alejandra es:", telefonoAlejandra)
print("El telefono de Alvaro es:", telefonoAlvaro)
print("El telefono de Atilio es:", telefonoAtilio)

# Los diccionarios tienen funciones de altas, bajas y modificaciones
agendaDeTelefonos["Juan"] = "11-2716-9270"

print(agendaDeTelefonos)