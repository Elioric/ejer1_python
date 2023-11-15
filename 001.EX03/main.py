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

rectangle_1: Rectangle = Rectangle(Point(),Point(0,7),Point(7,3),Point(3,0))
rectangle_2: Rectangle = Rectangle(Point(2,0),Point(2,6),Point(4,6),Point(4,0))

print(rectangle_1.height())
print(rectangle_1.base())
print(rectangle_2.height())

# print(rectangle_2)