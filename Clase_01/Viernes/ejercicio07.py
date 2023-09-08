# vamos a declarar un diccionario con números de telefono
agendaDeTelefonos = {
    "Alejandra": "4444-4444",
    "Alvaro": "5555-5555",
    "Atilio": "6666-6666"
}

# Mostramos nuestro diccionario en pantalla
print(agendaDeTelefonos)

# Vamos a acceder a los valores del diccionario a partir de sus claves o llaves
telefonoDeAlejandra = agendaDeTelefonos["Alejandra"]
telefonoDeAlvaro = agendaDeTelefonos["Alvaro"]
telefonoDeAtilio = agendaDeTelefonos["Atilio"]

# Imprimimos los telefonos
print("El telefono de Alejandra es:", telefonoDeAlejandra)
print("El telefono de Alvaro es:", telefonoDeAlvaro)
print("El telefono de Atilio es:", telefonoDeAtilio)

# Los diccionarios tienen funciones de altas, bajas y modificaciones

## Vamos a dar de alta un nuevo número
agendaDeTelefonos["David"] = "7777-7777"
print(agendaDeTelefonos)

## Modificamos el número de David
agendaDeTelefonos["David"] ="7777-8888"
print(agendaDeTelefonos)

## Vamos a borrar una llave
del agendaDeTelefonos["Atilio"]
print(agendaDeTelefonos)