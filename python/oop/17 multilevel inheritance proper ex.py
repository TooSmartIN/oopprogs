class gm:
    def __init__(self):
        self.gmage = 78
        self.mtage = 48
        self.dtage = 18

class mot(gm):
    def motname(self):
        return("mrs. abc")

class dghtr(mot):
    def dghtrname(self):
        return("ms. xyz")

    def totage(self):
        return(self.gmage + self.mtage + self.dtage)

d = dghtr()

print(d.motname())
print(d.totage())