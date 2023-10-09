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
            return "El monto de déposito debe ser mayor que cero."
    
    # Creamos un metodo para retirar dinsero comparando las cantidades para evitar saldo negativo y advertir de fondos insuficientes
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso. Saldo actual: {self.saldo}'
        else:
            return "Fondos insuficientes para realizar está transacción"
    
    # Creamos un metodo para obtener saldo
    def obtener_saldo(self):
        return f'Saldo actual de la cuenta: {self.saldo}'
    
# Creamos una clase de cuenta corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_cuenta, saldo, sobregiro):
        super().__init__(nombre_cuenta, saldo)
        self.sobregiro = sobregiro
    
    # Creamos un metodo para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo + self.sobregiro:
                self.saldo -= cantidad
                return f'Retiroso exitoso. Saldo actual: {self.saldo}'
            else:
                return f'Excede el limite de sobregiro permitido'
        else:
            return f'El monto de retiro debe ser mayor que cero.'
        
# Creamos una clase caja de ahorro
class CajaDeAhorro(CuentaBancaria):
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return f'Retiro exitoso. Saldo actual: {self.saldo}'
        else:
            return "Fondos insuficientes para realizar está transacción"
        

# Ejemplo de uso
if __name__ == "__main__":
    cuentas = [CuentaCorriente("Cuenta Corriente", 1000, 500), CajaDeAhorro("Caja de ahorro", 1500)]
    

    for cuenta in cuentas:
        print(f"Cuenta: {cuenta.nombre_cuenta}")
        print(cuenta.depositar(200))
        print(cuenta.retirar(1800))
        print(cuenta.retirar(200))
        print(cuenta.obtener_saldo())
        print("*" * 30)