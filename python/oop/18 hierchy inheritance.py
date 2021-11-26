class pet:
    def __init__(self, name):
        self.name = name

class dog(pet):
    def dgfeature(self):
        print(self.name, "does barking")

class cat(pet):
    def ctfeature(self):
        print(self.name, "does barking")

d = dog("tommy dog")
d.dgfeature()

c = cat("tom cat")
c.ctfeature()
