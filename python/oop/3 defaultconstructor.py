class Sq:
    def __init__(self):
        self.n = 9

    def sqr(self):
        return (self.n * self.n)

sq1 = Sq()
sq2 = Sq()
sq2.n = 10

print("the square of", sq1.n, "is = ", sq1.sqr())
print("the square of", sq2.n, "is = ", sq2.sqr())