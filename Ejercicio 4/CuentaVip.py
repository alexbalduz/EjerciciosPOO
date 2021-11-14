from CuentaBancaria import CuentaBancaria
from datetime import date

class CuentaVip(CuentaBancaria):
    def __init__(self, ID, titular, fecha_apertura, numero_cuenta, saldo, saldo_negativo):
        self.saldo_negativo = saldo_negativo
        super().__init__(ID, titular, fecha_apertura, numero_cuenta, saldo)

    def retirar_dinero(self, dinero):
        if float(dinero) > CuentaBancaria.getsaldo() + self.saldo_negativo:
            print('No hay suficiente dinero para retirar')
        else:
            dinero_final = (CuentaBancaria.getsaldo()) - float(dinero)
            CuentaBancaria.setsaldo(dinero_final)