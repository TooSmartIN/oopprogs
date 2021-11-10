'''create a class rectangle with attribs lenght and width and method is area . derive an object while supplying lenght = 10 and width = 20 and display the area'''

class Rectangle:

    def __init__(self, l, w):
        self.len = l
        self.wid = w

    def area(self):
        return(self.len*self.wid)

rc = Rectangle(10,20) 

print("the area of rectangle with length", rc.len,"and width", rc.wid, "is: ", rc.area())
