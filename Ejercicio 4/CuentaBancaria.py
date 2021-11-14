class CuentaBancaria():
    def __init__(self, ID, titular, fecha_apertura, numero_cuenta, saldo):
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
        if float(dinero) > CuentaBancaria.getsaldo():
            print('No hay suficiente dinero para retirar')
        else:
            dinero_final = (CuentaBancaria.getsaldo()) - float(dinero)
            CuentaBancaria.setsaldo(dinero_final)

    #Método para ingresar dinero
    def ingresar_dinero(self, dinero):
        dinero_final = (CuentaBancaria.getsaldo()) + float(dinero)
        CuentaBancaria.setsaldo(dinero_final)

    #Método para transferir dinero
    def transferir_dinero(self, dinero, cuenta):
        if float(dinero) > CuentaBancaria.getsaldo():
            print('No hay suficiente saldo para transferir')
        else:
            CuentaBancaria.retirar_dinero(dinero)
            cuenta.ingresar_dinero(dinero)
