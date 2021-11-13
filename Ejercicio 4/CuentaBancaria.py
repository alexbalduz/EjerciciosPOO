class CuentaBancaria():
    def __init__(self):
        self.ID = ''
        self.titular = ''
        self.fecha_apertura = ''
        self.numero_cuenta = 0
        self.saldo = 0

    #Definimos constructor
    def cuentaBancaria(self, ID, titular, fecha_apertura, numero_cuenta, saldo):
        self.ID = ID
        self.titular = titular
        self.fecha_apertura = fecha_apertura
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

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

    #Método get
    def getID(self):
        return self.ID

    def gettitular(self):
        return self.titular

    def getfecha_apertura(self):
        return self.fecha_apertura

    def getnumero_cuenta(self):
        return self.numero_cuenta

    def getsaldo(self):
        return self.saldo

    #Método para retirar dinero
    def retirar_dinero(self, dinero):
        if int(dinero) > CuentaBancaria.getsaldo():
            print('No hay suficiente dinero para retirar')
        else:
            dinero_final = (CuentaBancaria.getsaldo()) - int(dinero)
            CuentaBancaria.setsaldo(dinero_final)

