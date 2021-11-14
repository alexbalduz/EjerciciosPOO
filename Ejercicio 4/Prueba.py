from CuentaBancaria import CuentaBancaria
from Cuenta_PlazoFijo import Cuenta_PlazoFijo
from CuentaVip import CuentaVip
from datetime import date
import random

def fecha_aleatoria():
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().toordinal()
    random_day = date.fromordinal(random.randint(start_dt, end_dt))
    return random_day

def num_aleatorio():
    return random.randint(100000000000, 999999999999)

cuenta1 = CuentaBancaria(1, 'Alejandro', fecha_aleatoria(), num_aleatorio(), 10000)
cuenta2 = Cuenta_PlazoFijo(fecha_aleatoria(), 2, 'Pablo', fecha_aleatoria(), num_aleatorio(), 10000)
cuenta3 = CuentaVip(3, 'Angela', fecha_aleatoria(), num_aleatorio(), 10000, 100)

cuenta1.transferir_dinero(2000, cuenta2)
print(cuenta2.getsaldo())
print(cuenta1.getsaldo())
cuenta1.ingresar_dinero(575)
print(cuenta1.getsaldo())
cuenta1.retirar_dinero(78)
print(cuenta1.getsaldo())