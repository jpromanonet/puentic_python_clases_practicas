# Importarmos los modulos
import string
import sys

# Creamos una clase para contar caracteres
class CharCounter:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.char_count = {}
    
    # Creamos un metodo para contar caracteres en general
    def count_unique_chars(self):
        with open(self.input_filename, "r") as file:
            for line in file:
                for char in line:
                    if char.isalnum() or char is string.punctuation:
                        if char in self.char_count:
                            self.char_count[char] += 1
                        else:
                            self.char_count[char] = 1

    # Creamos un metodo para guardar el conteo en un archivo
    def write_char_count_to_file(self, output_filename):
        with open(output_filename, "w") as file:
            for char, count in self.char_count.items():
                file.write(f'{char} : {count}\n')

# Iniciamos el script
if __name__ == "__main__":
    input_filename = "./random_password.txt"
    output_filename = "conteo.txt"

    # Instanciamos un objeto de conteo
    character_count = CharCounter(input_filename)
    character_count.count_unique_chars()
    character_count.write_char_count_to_file(output_filename)
    print(f'El conteo de caracteres se ha guardado en {output_filename}.')