class CricketPlayer:
    def __init__(self):
        self.name = None
        self.match_played = None
        self.runs = None
        self.bat_avg = None
    
    def playerInput(self):
        self.name = input("Enter player name: ")
        self.match_played = int(input("Enter number of matches played: "))
        self.runs = int(input("Enter total number of runs scored: "))

    def battingAvg(self):
        self.bat_avg = self.runs / self.match_played
        print("Batting Average: %.2f" % self.bat_avg)
    
    def displayDetails(self):
        self.battingAvg()
        print("Name: ", self.name)
        print("Matches Played: ", self.match_played)
        print("Runs Scored: ", self.runs)
        print("Batting Average: ", self.bat_avg)


#Main Code

#Object Creation
player1 = CricketPlayer()
player2 = CricketPlayer()
player3 = CricketPlayer()
player4 = CricketPlayer()
player5 = CricketPlayer()

#Taking Player Details
print("Enter Details of Player1: ")
player1.playerInput()

print("\nEnter Details of Player2: ")
player2.playerInput()

print("\nEnter Details of Player3: ")
player3.playerInput()

print("\nEnter Details of Player4: ")
player4.playerInput()

print("\nEnter Details of Player5: ")
player5.playerInput()

#Calculating & Displaying Batting Averages for all Players
print("\nPlayer 1's", end=" ")
player1.battingAvg()
print("Player 2's", end=" ")
player2.battingAvg()
print("Player 3's", end=" ")
player3.battingAvg()
print("Player 4's", end=" ")
player4.battingAvg()
print("Player 5's", end=" ")
player5.battingAvg()

#Comparing Batting Averages
#Minimum
if (player1.bat_avg < player2.bat_avg) and (player1.bat_avg < player3.bat_avg) and (player1.bat_avg < player4.bat_avg) and (player1.bat_avg < player5.bat_avg):
    print("\nDetails of player with Minimum Batting Average: ")
    player1.displayDetails()
elif (player2.bat_avg < player1.bat_avg) and (player2.bat_avg < player3.bat_avg) and (player2.bat_avg < player4.bat_avg) and (player2.bat_avg < player5.bat_avg):
    print("\nDetails of player with Minimum Batting Average: ")
    player2.displayDetails()
