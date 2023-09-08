# Tenemos una lista con los datos personales de un usuario
datosPersonales = ["Pablo", "Romano", "11111111", 1989, "CABA", "Tierra del Fuego", "Membrillo"]

# Creamos un diccionaro que consuma datos desde una lista
usuario = {
    "Nombre": datosPersonales[0],
    "Apellido": datosPersonales[1],
    "DNI": datosPersonales[2],
    "Nacimiento": datosPersonales[3],
    "Ciudad de residencia": datosPersonales[4],
    "Ciudad de nacimiento": datosPersonales[5],
    "Clave": datosPersonales[6]
}

# Le pedimos al usuario que ingrese la clave
clave = input("Introduzca su contraseña: ")

if(usuario["Clave"] == clave):
    print("Bienvenido", usuario["Nombre"])
else:
    print("Contraseña incorrecta")