class CuentaBancaria(object):
    def __init__(self):
        self.ID = ''
        self.titular = ''
        self.fecha_apertura = ''
        self.numero_cuenta = 0
        self.saldo = 0
#Definimos constructor
    def cuentaBancaria(self, ID, titular, fecha_apertura, numero_cuenta):
        self.ID = ID
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
