
class Pattern:

    def ptrn(self):
        self.n = 65

        for i in range(0,5):
            for j in range(0,i+1):
                char = chr(self.n)
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
                self.n += 1
            print()

    
n = Pattern()
n.ptrn()