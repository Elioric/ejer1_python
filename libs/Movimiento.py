class Movimiento():
    
    """Se realiza un movimiento en una cuenta
       :param concepto: descripcion
       :param cantidad: cantidad
    """
    
    def __init__(self, concepto, cantidad):
        self.__concepto:str = concepto
        self.__cantidad:float = cantidad
        
    def __str__(self) -> str:
        return f"concepto: {self.__concepto}, cantidad: {self.__cantidad}"
    
    @property    
    def concepto(self) -> str:
        return self.__concepto
    
    @property
    def cantidad(self) -> float:
        return self.__cantidad
    
    # @cantidad.setter
    # def cantidad(self, cantidad) -> None:
    #     self.__cantidad = cantidad
    

# movimiento1 = Movimiento("matricula", 1000000)
# print(movimiento1)
# print(movimiento1.cantidad)
# movimiento1.cantidad = 2500000
# print(movimiento1.cantidad)