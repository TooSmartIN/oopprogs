'''create a class result. accept the marks from the user and display the grade as per the criteria <50: fail; <60d; '''


class Result:
    
    def __init__(self, marks):
        self.__mrk = marks

    def grade(self):

        if (self.__mrk < 50):
            return ("fail")
        elif(self.__mrk < 60):
            return("d")
        elif(self.__mrk < 70):
            return("c")
        elif(self.__mrk < 80):
            return("b")
        elif(self.__mrk < 90):
            return("a")
        elif(self.__mrk < 100):
            return ("entered marks are invalid")

    def getMarks(self):
        return self.__mrk


n = int(input("enter your marks for grading: "))
rslt = Result(n)
print("for your scored marks", rslt.getMarks(), "your grade is :", rslt.grade())