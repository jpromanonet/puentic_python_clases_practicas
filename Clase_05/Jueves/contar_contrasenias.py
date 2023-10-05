"""b. Desarrolle un programa que lea el archivo random_passwords.txt generado en el ejercicio anterior y escriba en un archivo llamado conteo.txt la cantidad de caracteres distintos que se encuentran en el archivo leído, por ejemplo, si encuentra 5 letras “a” minuscula debe escribir a 5."""

# Primero vamos a importar los modulos que necesitamos
import random
import string
import sys

# Vamos a crear una función para contar caracteres especiales
def count_unique_characters(filename):
    character_count = {}
    with open(filename, "r") as file:
        for line in file:
            for char in line:
                if char.isalnum() or char in string.punctuation:
                    if char in character_count:
                        character_count[char] += 1
                    else:
                        character_count[char] = 1
    return character_count

# Creamos una función para guardar el conteo en un archivo
def write_character_count_to_file(character_count, output_filename):
    with open(output_filename, "w") as file:
        for char, count in character_count.items():
            file.write(f"{char} {count}\n")

# Iniciamos el script
if __name__ == "__main__":
    input_filename = "./random_passwords.txt"
    output_filename = "conteo.txt"

    character_count = count_unique_characters(input_filename)
    write_character_count_to_file(character_count, output_filename)
    print(f'El conteo de caracteres se ha guardado en {output_filename}.')