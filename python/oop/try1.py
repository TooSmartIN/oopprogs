'''
# Python program to demonstrate
# command line arguments
 
 
import sys
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
     
# Addition of numbers
Sum = 0
# Using argparse module
for i in range(1, n):
    Sum += int(sys.argv[i])
     
print("\n\nResult:", Sum)


'''




















n = 65
for i in range(0,5):
            for j in range(0,i+1):
                char = chr(n)
                if i%2==0:
                    if not j%2==0 :
                        print(char.lower(),end="")
                    else :
                        print(char, end="")
                else :
                    if  j%2==0 :
                        print(char.lower(),end="")
                    else :
                        print(char, end="")
                n += 1
            print()
        

