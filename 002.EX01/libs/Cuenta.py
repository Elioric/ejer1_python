from libs.Cliente import Cliente
from libs.Movimiento import Movimiento

class Cuenta():
    
    __numero_cuenta:int = 1000
    __coleccion_cuentas = {}
    
    def __init__(self, titular:Cliente, saldo:float, tipo = "Ahorros"):
        self.__titular:Cliente = titular
        self.__saldo: float = saldo
        self.__movimientos: list = []
        self.__tipo:str = tipo
        self.__class__.__aumentaID()
        self.__numero: int = self.__class__.__obtenerId(self.__class__)
        self.__class__.__setColeccionCuentas(self)
    
    def __str__(self):
        return f"Cuenta {self.__tipo} no.: {self.__numero}, titular: {self.__titular}, el saldo actual es: {self.__saldo}. Se han realizado {len(self.__movimientos)} movimientos"
    
    def __repr__(self):
        return f"Cuenta {self.__tipo} no.: {self.__numero}, titular: {self.__titular}, el saldo actual es: {self.__saldo}. Se han realizado {len(self.__movimientos)} movimientos"
    
    @classmethod
    def __aumentaID(cls):
        """Aumenta el numero de la cuenta (ID) a medida de que se van creando cuentas en el banco
        
        :param cls: clase
        """
        cls.__numero_cuenta += 1
    
    def __obtenerId(cls):
        return cls.__numero_cuenta
    
    @classmethod
    def getColeccionCuentas(cls):
        return cls.__coleccion_cuentas
    
    @classmethod
    def __setColeccionCuentas(cls, obj_cuenta):
        cls.__coleccion_cuentas[obj_cuenta.numero] = obj_cuenta.__str__()
        
    @property
    def numero(self) -> int:
        return self.__numero
    
    @property
    def titular(self) -> Cliente:
        return self.__titular
    
    @property
    def saldo(self) -> float: 
        return self.__saldo
    
    @property
    def tipo(self) -> str:
        return self.__tipo
    
    def doMovimiento(self, concepto:str, cantidad:float) -> None:
        if self.__saldo >= cantidad:
            self.__saldo = self.__saldo - cantidad
            movimiento = (concepto, cantidad)
            self.__addMovimiento(movimiento)
        else:
            print("No se puede realizar la acción, saldo insuficiente!!!!")
    
    def __addMovimiento(self, movimiento) -> None:
        self.__movimientos.append(movimiento)
        
        
# cliente1 = Cliente("001","santisaza","morales")
# cliente2 = Cliente("002","kapaez","hooker")
# cuenta1 = Cuenta(cliente1,3600)
# cuenta2 = Cuenta(cliente2,0)
# print(cuenta1)
# print(cuenta2)
# print(Cuenta.cuenta)
# saludo = "hola"
# print(f"{saludo:>05}")