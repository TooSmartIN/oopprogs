class Sq:
    def __init__(self, no):
        self.n = no

    def sqr(self):
        return (self.n * self.n)

sq1 = Sq(9)
sq2 = Sq(10)


print("the square of", sq1.n, "is = ", sq1.sqr())
print("the square of", sq2.n, "is = ", sq2.sqr())