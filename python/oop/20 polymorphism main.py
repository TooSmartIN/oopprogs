class rect:
    def __init__(self):
        self.l = 10
        self.w = 20

    def area(self):
        print("the rect area is = ", self.l*self.w)

    def somemethod(self):
        print("just to check ..")

class sq(rect):

    def area(self):
        print("the square area: =", self.l*self.l)


s = sq()
s.area()
s.somemethod()