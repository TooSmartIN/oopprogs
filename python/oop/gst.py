class Gst:

    __amt = 0
    __taxamount = 0

    def __init__(self, x):
        self.__amt = x


    def tax(self):
        a = (self.__amt * 18/100)
        self.__taxamount = a + self.__amt
        return a

    def getAmt(self):
        return self.__amt

    def getAmtTX(self):
        return (self.__taxamount)


'''
n = int(input("enter the bill amount: "))'''
n = 1000

bill1 = Gst(n)

print("a = ", bill1.getAmt(), " b = ",bill1.tax()," c = ",bill1.getAmtTX()  )

