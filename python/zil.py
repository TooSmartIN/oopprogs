class AutoServiceStation:
 
    def __init__(self,empid,empname,basicsalary,empexp): # Constructor
        self.emp_id=empid
        self.emp_name=empname
        self.basic_salary=basicsalary
        self.emp_exp=empexp


    def calculate_salary(self): #function name must be a verb
        self.hra = 0.35*self.basic_salary
        self.da = 0.58*self.basic_salary
        self.pf = 0.095*self.basic_salary
        self.sums = self.hra+self.da-self.pf
        return self.sums

    def calculate_bonus(self):
        self.year = self.emp_exp
        self.bonus=0

        if(self.year>=30):
            self.bonus = 1.59*self.basic_salary
        elif(self.year>=23):
            self.bonus = 1.51*self.basic_salary
        elif(self.year>=15):
            self.bonus = 1.45*self.basic_salary
        elif(self.year>=7):
            self.bonus = 1.33*self.basic_salary
        elif(self.year<7):
            self.bonus = 1.16*self.basic_salary

            return self.bonus

    def display(self):
        print("\nName:",self.emp_name)
        print("\nBasic Salary:",self.basic_salary)
        print("\nExperience:",self.emp_exp)
        print("\nNet Salary:",self.basic_salary+self.sums+self.bonus)


empid=input("Enter your employee id :")
empname=input("Enter your name :")
basicsalary=int(input("Enter your Basic salary :"))
empexp=int(input("Enter years of experience :"))


n1 = Employee(empid,empname,basicsalary,empexp)
n1.calculate_salary()
n1.calculate_bonus()
n1.display()