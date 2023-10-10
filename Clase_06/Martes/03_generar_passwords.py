# Primero vamos a importar los modulos que necesitamos
import random
import string
import sys

# Creamos una clase para generar contraseñas
class PasswordGenerator:
    def __init__(self, length = 16):
        self.length = length
    
    # Creamos un metodo que genere contraseñas aleatorias
    def generate_random_passwords(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password
    
    # Creamos un metodo que escriba las contraseñas en un archivo
    def write_random_passwords(self, num_passwords):
        with open("random_password.txt", "w") as file:
            for _ in range(num_passwords):
                password = self.generate_random_passwords()
                file.write(password + '\n')

# Ejecutamos los metodos.
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 03_generar_passwords.py <cantidad de contraseñas que queremos generar>")
        sys.exit(1)

    # Tomar por parametros la cantidad de contraseñas a generar
    num_password = int(sys.argv[1])

    # Instancioamos un objeto de la clase PasswordGenerator
    password_generator = PasswordGenerator()
    password_generator.write_random_passwords(num_password)
    print(f'Se han generado {num_password} contraseñas aleatorias en random_passwords.txt')