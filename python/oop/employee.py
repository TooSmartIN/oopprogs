class Employee:


    def __init__(self):
        
        self.__basicsalary = 0
        self.__name = ''
        self.__empid = 000000
        self.__exp = 0
        self.__hra = .35
        self.__da = .58
        self.__pf = .095
        self.__bonus = 0

    def setSal(self, sal):
        self.__basicsalary = sal
    
    def setEmpid(self, id):
        self.__empid = id

    def setExp(self, exp):
        self.__exp = exp

    def setName(self, nam):
        self.__name = nam

    def calbonus(self):

        if(self.__exp >= 30):
            self.__bonus = self.__basicsalary * .59
        elif(self.__exp >= 23):
            self.__bonus = self.__basicsalary * .51
        elif(self.__exp >= 15):
            self.__bonus = self.__basicsalary * .45
        elif(self.__exp >= 7):
            self.__bonus = self.__basicsalary * .33
        elif(self.__exp < 7):
            self.__bonus = self.__basicsalary * .16

        return self.__bonus

    def netsal(self):
        self.__netsal = self.__basicsalary + ( self.__basicsalary * self.__da ) + (self.__basicsalary * self.__hra) - ( self.__basicsalary * self.__pf) + self.__bonus
        return self.__netsal
 

'''
a = int(input("enter employee id: "))
b = input("name: ")
c = int(input("basic salary: "))
d = int(input("no. of yrs in experiance: ")
'''


a = 556631
b = 'hehelol' 
c = 50000
d = 16

emp = Employee()

emp.setSal(c)
emp.setName(b)
emp.setEmpid(a)
emp.setExp(d)


print(emp.netsal())


