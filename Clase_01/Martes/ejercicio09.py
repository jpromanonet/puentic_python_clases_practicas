# 1. Cree un diccionario llamado ingredientes que contenga como clave nombres de ingredientes y como valor su cantidad según alguna receta de cocina.

# 2. Utilizando la lista persona cree un diccionario llamado usuario que reemplace la estructura de lista creada con sus respectivas claves y valores. TIP: dict = {“clave”:”valor”}

# Ejercicio 1

ingredientesDeTorta = {
    "harina": 200,
    "azucar": 100,
    "huevos": 3,
    "leche": 250,
    "cacao": 150,
    "polvoDeHornear": 10,
    "nueces": 50
}

print(ingredientesDeTorta)

# Ejercicio 2

## Vamos a crear una lista con los datos personales del usuario
datosPersonales = ["Pablo", "Romano", 11222333, 1994 ,"CABA", "Tierra del Fuego", "Membrillo"]

# Creamos un diccionario que se alimente de la lista de datos personales
usuario = {
    "Nombre": datosPersonales[0],
    "Apellido": datosPersonales[1],
    "DNI": datosPersonales[2],
    "Nacimiento": datosPersonales[3],
    "Ciudad de residencia": datosPersonales[4],
    "Ciudad de nacimiento": datosPersonales[5],
    "Clave": datosPersonales[6]
}

# Imprimimos nuestro diccionario
print(usuario)