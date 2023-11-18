from libs.geometry.elements import (Point,
                                    Line,
                                    Rectangle)
from libs.decorators.messages import calculus

vertex_1:Point = Point()
vertex_2:Point = Point(0,7)
vertex_3:Point = Point(3,7) 
vertex_4:Point = Point(3,0)

# print(vertex_1)
# print(vertex_1.__repr__())
# print(vertex_3.x)
# print(vertex_3.x)

print("coordenadas:", vertex_1.coordinates)
vertex_1.x = 3
vertex_1.y = 3
print("coordenadas:", vertex_1.coordinates)

rectangle_1: Rectangle = Rectangle(Point(),Point(0,7),Point(7,3),Point(3,0))
rectangle_2: Rectangle = Rectangle(Point(2,0),Point(2,6),Point(4,6),Point(4,0))
rectangle_3: Rectangle = Rectangle(height=15,base=5)

print(rectangle_1.height())
print(rectangle_1.base())

print(rectangle_1.__dict__)
print(rectangle_2.height())
print(rectangle_2.height())
print(rectangle_3.height())

print("area 1:", rectangle_1.area())
print("area 2:", rectangle_2.area())
print("area 3:", rectangle_3.area())

print("rectangulo 1 vertices:", rectangle_1)
print("se realiza desplazamiento")
rectangle_1.traslacion(2,3)
print("se realizó desplazamiento")
print("rectangulo 1 vertices:", rectangle_1)

# print(rectangle_2)

def prueba_pos_args_kwargs(color, /, vertex_1:Point, vertex_2:Point, vertex_3:Point, vertex_4:Point, *, height:float, base:float) -> None:
    print(color)
    print(vertex_1, vertex_2, vertex_3, vertex_4)
    print(height, base)


# print("-"*30)
# prueba_pos_args_kwargs("verde", 1,2,3,4, height=13, base=7)
# print("-"*30)
# prueba_pos_args_kwargs("verde", 1, vertex_2=2, vertex_3=3, vertex_4=4, height=13, base=7)
# print("-"*30)
# prueba_pos_args_kwargs("verde", vertex_1=1, vertex_2=2, vertex_3=3, vertex_4=4, height=13, base=7)


# if (0,):
#     print("iguales")
    
# if 2 and -1 and 4:
#     print("entró al condicional")