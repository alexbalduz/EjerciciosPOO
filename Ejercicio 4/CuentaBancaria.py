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

    #Método set
    def setID(self, ID):
        self.ID = ID

    def settitular(self, titular):
        self.titular = titular

    def setfecha_apertura(self, fecha_apertura):
        self.fecha_apertura = fecha_apertura

    def setnumero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def setsaldo(self, saldo):
        self.saldo = saldo

