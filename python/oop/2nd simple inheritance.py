class rect:
    def __init__(self):
        self.l = 10
        self.w = 20


    def Rectarea(self):
        return (self.l*self.w)


class sq(rect):

    def sqarea(self):
        return(self.l*self.l)



r1 = rect()
print("the area is ", r1.Rectarea())

s1 = sq()
print("the area is", s1.sqarea())