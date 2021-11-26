##write a program
##create a class circle with radius attribute and method to calculate area
##create an object for radius = 10 and display area

"""
##my answer
class circle(self):
    r = 10
    pi = 22/7
    print(pi*r*r)

Val = circle()
"""


###actual answer
class circle():
    r = 0

    def area(self):
        return(3.14*self.r*self.r)

crcl = circle()
crcl.r = 10


print("the area of the circle with radius", crcl.r, ":", crcl.area() )

