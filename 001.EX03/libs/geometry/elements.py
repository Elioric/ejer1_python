from libs.decorators.messages import calculus

class Manipulation:
    
    def draw():
        pass
    
class Figure:
    
    def __init__(self, *args, **kwargs) -> None:
        self.__vertexes=()

class Point:
    
    def __init__(self, x:float = 0, y:float = 0) -> None:
        self.__coordinates:tuple = tuple([x,y])

    def __str__(self) -> str:
        return f"[str] x-coordinate is: {self.__coordinates[0]} and y-coordinate is: {self.__coordinates[1]}"
    
    def __repr__(self) -> str:
        return f"P: ({self.__coordinates[0]}, {self.__coordinates[1]})"

    @property
    def coordinates(self) -> tuple:
        return self.__coordinates()
    
    @coordinates.setter
    def coordinates(self,x,y) -> None:
        self.__coordinates:tuple = tuple([x,y])
        
    @property
    def x(self) -> tuple:
        return self.__coordinates[0]
    
    @property
    def y(self) -> tuple:
        return self.__coordinates[1]
    
    @staticmethod
    def distance_between_points(P:tuple, Q:tuple) -> float:
        pass
        
class Line:
    """Define una recta a partir de dos puntos
    """
    
    def __init__(self, P:Point = Point(), Q:Point = Point()) -> None:
        self.__initial_point = P
        self.__final_point   = Q
        self.__m = self.calculate_slope(P, Q)
    
    @staticmethod    
    def calculate_slope(P, Q):
        m = (Q.coordinates[1] - P.coordinates[1])/(Q.coordinates[0] - P.coordinates[0])
        return m

    @staticmethod
    def length_of_segment(P:Point, Q:Point) -> float:
        """Calcula la longitud del segmento definido por dos puntos

        :param P: punto inicial
        :type P: Point
        :param Q: punto final
        :type Q: Point
        :return: longitud del segmento comprendido por los dos puntos
        :rtype: float
        """
        length = ( (Q.x - P.x)**2 + (Q.y - P.y)**2 ) ** (0.5)
        return length
        
class Rectangle:
    """Define un rectángulo a partir de 4 vértices
    """
    
    # def __init__(self, height:float, base:float) -> None:
    #     self.__height: float  = height
    #     self.__base: float    = base
        
    def __init__(self, vertex_1:Point, vertex_2:Point, vertex_3:Point, vertex_4:Point) -> None:
        self.__vertexes:tuple = tuple([vertex_1,vertex_2,vertex_3,vertex_4])
        
    def __str__(self) -> str:
        return f"[str] The vertexes of the rectangle are: {self.vertexes}"
    
    def __repr__(self) -> str:
        return f"P:{self.vertexes}"        
    
    @property    
    def vertexes(self):
        return self.__vertexes
    
    def height(self):
        return Line.length_of_segment(self.__vertexes[0], self.__vertexes[1])

    # @calculus
    def base(self):
        return Line.length_of_segment(self.__vertexes[0], self.__vertexes[3])

    @staticmethod
    def area():
        pass
    
    
    # @coordinates.setter
    # def coordinates(self,x,y):
    #     self.__coordinates:tuple = tuple([x,y])
        
    