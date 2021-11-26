#getter

class Sq1:
    def __init__(self):
        self.__no = 9

    def getSq(self):
        return (self.__no * self.__no)

    def getNo(self):
        return self.__no
        
s1 = Sq1()
print("the sqr is ", s1.getSq())
print("the value of the attribute is ", s1.getNo() )






#setter

class Sq2:

    def __init__(self):
        self.__no = 9

    def getSq(self):
        return(self.__no*self.__no)

    def setNo(self, n):
        self.__no = n


s2 = Sq2()
n = int(input("pls enter the number"))
s2.setNo(n)

print("the sqr is = ", s2.getSq())