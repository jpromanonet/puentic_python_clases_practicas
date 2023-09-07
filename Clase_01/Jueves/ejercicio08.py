# Vamos a crear una lista con los datos personales de un usuario
datosPersonales = ["Juan", "Romano", 11111112, 1994,"CABA", "Tierra del Fuego", "Membrillo"]

# Creamos un diccionario que consuma datos desde una lista
usuario = {
    "Nombre": datosPersonales[0],
    "Apellido": datosPersonales[1],
    "DNI": datosPersonales[2],
    "Nacimiento": datosPersonales[3],
    "Ciudad de residencia": datosPersonales[4],
    "Ciudad de nacimiento": datosPersonales[5],
    "Clave": datosPersonales[6]
}

# Imprimimos nuestro usuario
print(usuario)