# Importamos los modulos
import string
import sys

# Creamos una clase para contar caracteres
class ContarCaracteres:
    def __init__(self, input_file):
        self.input_file = input_file
        self.char_count = {}
    
    # Creamos un metodo para contar
    def contar(self):
        with open(self.input_file, "r") as file:
            for line in file:
                for char in line:
                    if char.isalnum() or char is string.punctuation:
                        if char in self.char_count:
                            self.char_count[char] += 1
                        else:
                            self.char_count[char] = 1
    
    # Crear un metodo para guardar el conteo en un archivo
    def guardar_conteo(self, output_file):
        with open(output_file, "w") as file:
            for char, count in self.char_count.items():
                file.write(f'{char} : {count}\n')

# Invocar a la clase
if __name__ == "__main__":
    input_file = "./randoms_passwords.txt"
    output_file = "conteo.txt"

    # Instanciamos el objeto de conteo
    contar = ContarCaracteres(input_file)
    contar.contar()
    contar.guardar_conteo(output_file)
    print(f'El conteo de caracteres se ha guardado en {output_file}.')