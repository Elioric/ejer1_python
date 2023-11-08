from libs.Cliente import Cliente
from libs.Cuenta import Cuenta

cliente1 = Cliente("1001","Antonio","Martinez")

cuenta1 = Cuenta(cliente1, 5600, "Corriente")

cuenta1.doMovimiento("Salario santisaza", 1000)
cuenta1.doMovimiento("Pago prestaciones", 30)
cuenta1.doMovimiento("Dentista", 100)
cliente2 = Cliente("001","santisaza","morales")
cliente3 = Cliente("002","kapaez","hooker")
cuenta2 = Cuenta(cliente2,3600)
cuenta3 = Cuenta(cliente3,0)

print(cuenta1)

print("La colección de cuentas:", Cuenta.getColeccionCuentas())