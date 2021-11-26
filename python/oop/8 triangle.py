'''create a class triangle with attribute base and height. method area (1/2 base * height). create the object by passing the value of base and height by object creation which values 10,20 and display the area'''


class Triangle:

    def __init__(self,b,h):
        self.__base = b
        self.__height = h

    def display_area(self):
        return (self.__base * self.__height * 1/2)

tri = Triangle(10,20)

print("the area of the triangle is ", tri.display_area())
