"""b. Desarrolle un programa que lea el archivo random_passwords.txt generado en el ejercicio anterior y escriba en un archivo llamado conteo.txt la cantidad de caracteres distintos que se encuentran en el archivo leído, por ejemplo, si encuentra 5 letras “a” minuscula debe escribir a 5."""

# Primero vamos a importar los modulos que necesitamos
import random
import string
import sys

# Creamos una clase para contar caracteres
class CharacterCounter:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.character_count = {}

    # Vamos a crear una función para contar caracteres especiales
    def count_unique_characters(self):
        with open(self.input_filename, "r") as file:
            for line in file:
                for char in line:
                    if char.isalnum() or char in string.punctuation:
                        if char in self.character_count:
                            self.character_count[char] += 1
                        else:
                            self.character_count[char] = 1

    # Creamos una función para guardar el conteo en un archivo
    def write_character_count_to_file(self, output_filename):
        with open(output_filename, "a") as file: # si queres sumarlo al archivo usas la "a" por APPEND y si queres sobre-escribirlo usa la "w" por WRITE
            for char, count in self.character_count.items():
                file.write(f"{char} {count}\n")

# Iniciamos el script
if __name__ == "__main__":
    input_filename = "./random_passwords.txt"
    output_filename = "conteo.txt"

    character_count = CharacterCounter(input_filename)
    character_count.count_unique_characters()
    character_count.write_character_count_to_file(output_filename)
    print(f'El conteo de caracteres se ha guardado en {output_filename}.')