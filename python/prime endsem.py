min = int(input("enter the first number: "))
max = int(input("enter the final number: "))

    
for num in range(min, max + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
