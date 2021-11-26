class sq:
    def __init__(self):
        self.l = 10

    def getarea(self):
        return(self.l*self.l)

class cube(sq):
    def getvol(self):
        return (self.l*self.l*self.l)

c1 = cube()
print("cube volumn is", c1.getvol())
print("square area is ", c1.getarea())

s1=sq()
print("the area of the square id ", s1.getarea())
