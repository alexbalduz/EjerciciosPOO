from CuentaBancaria import CuentaBancaria
from datetime import date
class Cuenta_PlazoFijo(CuentaBancaria):
    def __init__(self, fecha_vencimiento, ID, titular, fecha_apertura, numero_cuenta, saldo):
        self.fecha_vencimiento = fecha_vencimiento
        super().__init__(ID, titular, fecha_apertura, numero_cuenta, saldo)

    def retirar_dinero(self, dinero):
        if float(dinero) > self.getsaldo():
            print('No hay suficiente dinero para retirar')
        else:
            penalizacion = 0.0
            if date.today() < self.fecha_vencimiento:
                penalizacion = dinero * 0.05
            dinero_final = (self.getsaldo()) - float(dinero) - penalizacion
            self.setsaldo(dinero_final)