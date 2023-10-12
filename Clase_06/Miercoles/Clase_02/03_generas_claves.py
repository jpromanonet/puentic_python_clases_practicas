# Primero vamos a importar los modulos que necesitamos
import random
import string
import sys

# Creamos una clase para generar contraseñas
class PasswordGenerator:
    def __init__(self, length = 64):
        self.length = length
    
    # Creamos un metodo que genere contraseñas aleatorias
    def generate_random_passwords(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
    
    # Creamos un metodo que guarde las contraseñas en un archivo de texto
    def write_random_passwords(self, num_passwords):
        with open("randoms_passwords.txt", "w") as file:
            for _ in range(num_passwords):
                password = self.generate_random_passwords()
                file.write(password + "\n")
    
# Invocar a la clase de contraseñas
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 03_generar_claves.py <cantidad de claves a generar>")
        sys.exit(1)
    
    # Tomamos por parametro la cantidad de contraseñas a generar
    num_passwords = int(sys.argv[1])

    # Creamos el objeto de la clase PasswordGenerator
    password_generator = PasswordGenerator()
    password_generator.write_random_passwords(num_passwords)
    print(f'Se han generado {num_passwords} contraseñas aleatorias en random_passwords.txt')