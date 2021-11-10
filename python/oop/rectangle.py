"""
create a class rectangle having attribute lenght and breadth and methods to calculate area(l*w) and paramater(2[l+w])
l = 10 
w = 20
create an object """

class Rectangle:

    l = 0
    w = 0

    def area(self):
        return(self.l*self.w)

    def parameter(self):
        return(2*self.l + 2*self.w)
    

rc = Rectangle()

rc.l = 10
rc.w = 20

print(
    "the area of rectangle with length", rc.l,"and width", rc.w, "is: ", rc.area(), "and parameter is: ", rc.parameter()
    )
