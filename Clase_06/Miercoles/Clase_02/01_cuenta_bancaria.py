# Creamos una clase llamada cuenta bancaria
class CuentaBancaria:
    # Creamos un metodo constructor
    def __init__(self, nombre_cuenta, saldo):
        self.nombre_cuenta = nombre_cuenta
        self.saldo = saldo
    
    # Creamos un metodo de deposito
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f'Deposito exitoso, depositaste {cantidad}. Saldo actual: {self.saldo}.'
        else:
            return 'El monto de deposito debe ser mayor a cero.'
    
    # Metodo de retiro
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso, retiraste: {cantidad}. Saldo actual: {self.saldo}'
        else:
            return "Fondos insuficientes para realizar esta transacción."
    
    # Metodo para obtener saldo
    def obtener_saldo(self):
        return f'Saldo actual de la cuenta: {self.saldo}.'

# Declaramos una subclase de CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    # Creamos un constructor y heredamos del constructor de la clase padre
    def __init__(self, nombre_cuenta, saldo, sobregiro):
        super().__init__(nombre_cuenta, saldo)
        self.sobregiro = sobregiro
    
    # Re escribir el metodo retirar
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo + self.sobregiro:
                self.saldo -= cantidad
                return f'Retiro exitoso, retiraste {cantidad}. Saldo actual: {self.saldo}.'
            else:
                return f'Excede el limite descubierto permitido.'

# Creamos otra subclase para la caja de ahorro
class CajaAhorro(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso, retiraste: {cantidad}. Saldo actual: {self.saldo}.'
        else:
            return f'Fondos insuficientes para realizar está transacción.'

# Caso de uso
if __name__ == "__main__":
    # Anidamos las subclases en un solo objeto
    cuentas = [CuentaCorriente("Cuenta Corriente", 1000, 500), CajaAhorro("Caja de Ahorro", 1500)]

    # Vamos a recorrer el objeto por cada una de sus instancias, representadas en indices de una lista.
    for cuenta in cuentas:
        print("*" * 40)
        print(f'Cuenta: {cuenta.nombre_cuenta}')
        print(f'{cuenta.depositar(200)}')
        print(f'{cuenta.retirar(1800)}')
        print(f'{cuenta.retirar(200)}')
        print(cuenta.obtener_saldo())