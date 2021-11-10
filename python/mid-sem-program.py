import random
import time

class Dice:

    def dice_throw(self, sum):
        self.sum = sum
        print("Player 1 is throwing the dice")
        self.dice1 = random.randint(1, 7)
        self.dice2 = random.randint(1, 7)
        print(f"Player 1 throws the dice = {self.dice1} + {self.dice2} = ",(self.dice1 + self.dice2))
        self.sum.append(self.dice1 + self.dice2)
        print("\n")
        
        time.sleep(2)

        print("Player 2 is throwing the dice")
        self.dice1 = random.randint(1, 7)
        self.dice2 = random.randint(1, 7)
        print(f"Player 2 throws the dice = {self.dice1} + {self.dice2} = ",(self.dice1 + self.dice2))
        self.sum.append(self.dice1 + self.dice2)
        print("\n")

        return self.sum

    def result(self, sum):
        self.sum = sum
        self.sum1 = self.sum[0] + self.sum[2] + self.sum[4]
        self.sum2 = self.sum[1] + self.sum[3] + self.sum[5]
        print(f"Player 1 score = {self.sum1}") 
        print(f"Player 2 score = {self.sum2}")
        print("\n")
        if self.sum1 > self.sum2:
            print("YOOOHHOOO player 1 is the winner!!!")

        else:
            print("YYYOOOOHHOOO Player 2 is the  Winner!!!")    

player = Dice()
sum = []

for i in range(1,4):
    sum = player.dice_throw(sum)
    time.sleep(2)
    
player.result(sum)