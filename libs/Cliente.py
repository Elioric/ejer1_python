# from Movimiento import Movimiento

class Cliente():
    """Esta clase define un cliente del banco
       :param dni: numero de documento
       :param nombre: nombre del titular
       :param apellidos: apellidos del titular
    """

    def __init__(self, dni:str, nombre:str, apellidos:str):
        self.__dni:str = dni
        self.__nombre:str = nombre
        self.__apellidos:str = apellidos
        
    def __str__(self) -> str:
        return f"{self.__nombre} {self.__apellidos}"
        
# cliente = Cliente("","","")
# print(cliente)