class animal:
    def eat(self):
        print("eating ..")

class dog(animal):
    def bark(self):
        print("barking ..")

class babydog(dog):
    def weep(self):
        print("weeping ..")

d = babydog()

d.eat()
d.bark()
d.weep()