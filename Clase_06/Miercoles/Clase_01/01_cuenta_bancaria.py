# Creamos una clase llamada cuenta bancaria
class CuentaBancaria:
    def __init__(self, nombre_cuenta, saldo):
        self.nombre_cuenta = nombre_cuenta
        self.saldo = saldo

    # Creamos un metodo de depositos
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f'Deposito exitoso. Saldo actual: {self.saldo}'
        else:
            return "El mono de deposito debe ser mayor que cero."
    
    # Metodo de retiro
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso. Saldo actual: {self.saldo}'
        else:
            return "Fondos insuficientes para realizar está transacción."
        
    # Creamos un metodo para obtener el saldo
    def obtener_saldo(self):
        return f'Saldo actual de la cuenta: {self.saldo}'
    
# Creamos una subclase de cuenta corriente
class CuentaCorriente(CuentaBancaria):
    # Creamos un constructor y heredamos del constructor de la clase padre.
    def __init__(self, nombre_cuenta, saldo, sobregiro):
        super().__init__(nombre_cuenta, saldo)
        self.sobregiro = sobregiro

    # Creamos un metodo para retirar dinero con sobregiro
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo + self.sobregiro:
                self.saldo -= cantidad
                return f'Retiro exitoso. Saldo actual: {self.saldo}'
            else:
                return f'Excede el limite descubierto permitido.'

# Creamos otra subclase para la caja de ahorro
class CajaAhorro(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso. Saldo actual: {self.saldo}'
        else:
            return f'Fondos insuficientes para realizar está transacción.'
        
# Caso de uso
if __name__ == "__main__":
    cuentas = [CuentaCorriente("Cuenta Corriente", 1000, 500), CajaAhorro("Caja de Ahorro", 1500)]

    for cuenta in cuentas:
        print("*" * 40)
        print(f'Cuenta: {cuenta.nombre_cuenta}')
        print(cuenta.depositar(200))
        print(cuenta.retirar(1800))
        print(cuenta.retirar(200))
        print(cuenta.obtener_saldo())