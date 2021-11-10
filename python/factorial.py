def fact(n):
    ans = 1
    for i in range(n):
        ans = ans + (ans*i)    

    print(ans)

num = int(input("enter a number: "))
fact(num)