class sq:
    def __init__(self):
        self.l = 10

    def sqarea(self):
        return (self.l*self.l)


class rect(sq):
    def __init__(self):
        self.w = 30

        #super().__init__()   super() keyword is used to call parent .// note: self is not required
        sq.__init__(self)    #call the constructor using classname.constructor(self)

    def rectarea(self):
        return(self.l*self.w)

r1 = rect()

print("the area of rect = ", r1.rectarea())
