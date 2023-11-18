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
        return self.__coordinates
    
    @coordinates.setter
    def coordinates(self,coor) -> None:
        self.__coordinates = tuple(coor)
        
    @property
    def x(self) -> float:
        return self.__coordinates[0]
    
    @x.setter
    def x(self, x) -> float:
        self.coordinates = (x, self.y)
    
    @property
    def y(self) -> float:
        return self.__coordinates[1]
    
    @y.setter
    def y(self, y) -> float:
        self.coordinates = (self.x, y)
    
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
       :param vertex_1: vértice inferior izquierdo 
       los demás van en el sentido de las manecillas del reloj
    """
        
    def __init__(self, /, vertex_1:Point = tuple(), vertex_2:Point = tuple(), vertex_3:Point = tuple(), vertex_4:Point = tuple(), *, height:float = 0, base:float = 0) -> None:
        
        if vertex_1 and vertex_2 and vertex_3 and vertex_4:
            self.__vertexes:tuple = tuple([vertex_1,vertex_2,vertex_3,vertex_4])
        elif height and base:
            self.__height:float = height
            self.__base:float   = base
            self.__vertexes:tuple = tuple([Point(),Point(0,height),Point(base,height),Point(base,0)])
            
    def __str__(self) -> str:
        return f"[str] The vertexes of the rectangle are: {self.vertexes}"
    
    def __repr__(self) -> str:
        return f"P:{self.vertexes}"        
    
    @property    
    def vertexes(self) -> tuple:
        return self.__vertexes
    
    def height(self) -> float:
        if getattr(self, "_Rectangle__height", None):
            return self.__height
        else:
            self.__height = Line.length_of_segment(self.__vertexes[0], self.__vertexes[1])
            return self.__height

    def base(self) -> float:
        if getattr(self, "_Rectangle__base", None):
            return self.__base
        else:
            self.__base = Line.length_of_segment(self.__vertexes[0], self.__vertexes[3])
            return self.__base

    def area(self) -> float:
        return self.height() * self.base()
    
    def traslacion(self, x_des:float, y_des:float) -> None:
        """Traslada un rectangulo en el plano

        :param x_des: desplazamiento horizontal
        :type x_des: float
        :param y_des: desplazamiento vertical
        :type y_des: float
        """
        for punto in self.__vertexes:
            punto.x = punto.x + x_des
            punto.y = punto.y + y_des