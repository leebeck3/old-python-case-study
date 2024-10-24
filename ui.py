############################################
# Class: CPTR 226 - Computer Science I
# Assignment: Case Study ch11
# Author(s): Lee
# Date: 11/10/19
############################################

#imports
from db import *
from objects import Player,Lineup
import csv
from datetime import datetime, timedelta, date

#tuple
TeamPositionList = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

#intro
def menu():
    print("=" * 64)
    print("      Baseball Team Manager        ")
    print()
    print("CURRENT DATE (YYYY-MM-DD):  ", date.today())
    GameDate = str(input("GAME DATE (YYYY-MM-DD):     "))
    if GameDate == "":
        menuoptions()
    else:
        GameDate = datetime.strptime(GameDate, "%Y-%m-%d")
        DifferenceOfDays = GameDate-datetime.now()
        if DifferenceOfDays <= timedelta(days = 0):
            menuoptions()
        else:
            print("DAYS UNTIL GAME:", DifferenceOfDays.days)
            menuoptions()

#menu function
def menuoptions():
    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    print(TeamPositionList[0] + " , " + TeamPositionList[1]+ " , " +TeamPositionList[2]+ " , " +TeamPositionList[3]+ " , " +TeamPositionList[4]+ " , " +TeamPositionList[5]+ " , " +TeamPositionList[6]+ " , " +TeamPositionList[7]+ " , " +TeamPositionList[8])
    print()
    try:
        with open("player_list.csv") as file:
            print("File found")
    except FileNotFoundError:
        print("Team data file could not be found")
        print("You can create a new one if you want")
    print("=" * 64)

#batting average function
def battingaverage(x,y):
    if y > 0:
        BattingAverage = x / y
        BattingAverage = round(BattingAverage, 2)
        BattingAverage = str(BattingAverage)
        return BattingAverage
    else:
        BattingAverage = 0
        return BattingAverage

def ErrorCheckerAtBats(x):
    while True:
        if x < 0:
            print("Error, official times at bat can't be less than 0, please try again.")
            print()
            x = int(input("Official number of at bats: "))
        else:
            break

def ErrorCheckerHits(x,y):
    while True:
        if y > x:
            print("Error, official at bats can't be greater than number of hits please try again.")
            print()
            y = int(input("Number of hits: "))
            x = int(input("Official number of at bats: "))
        elif y < 0:
            print("Error, Can't have negative number of hits, please try again.")
            print()
            y = int(input("Number of hits: "))
        else:
            break

#main function
def main():
    menu()

    playerlist = read()
    players = Lineup(playerlist)



    while True:
        try:
            UserVariable = int(input("Menu option: "))
        except Exception as e:
            print("Not a valid option. Please try again.")
            continue
            
        if UserVariable == 1:#note couldn't add into Lineup becuase I couldn't get it to iterate
            print("{:>9} {:>30} {:>7} {:>7} {:>7}".format("Player", "POS", "AB", "H", "AVG"))
            print("-" * 64)
            PlayerFormat = "{:<2} {:<30} {:>6} {:>7} {:>7} {:>7}"
            counter = 1
            for player in playerlist:
                Name = str(player.FirstName) + " " + str(player.LastName)
                Position = player.Position
                AB = player.AtBats
                Hits = player.Hits
                Average = battingaverage(int(Hits), int(AB))
                print(PlayerFormat.format(counter,Name,Position,AB,Hits,Average))
                counter += 1
            print()
            
        elif UserVariable == 2:
            FirstName = str(input("First Name: "))
            LastName = str(input("Last Name: "))
            Position = (str(input("Position: ")))
            AtBats = int(input("At bats: "))
            ErrorCheckerAtBats(AtBats)
            Hits = int(input("Hits: "))
            ErrorCheckerHits(AtBats,Hits)
            players.AddPlayer(FirstName,LastName,Position,AtBats,Hits)
            continue
            
        elif UserVariable == 3:
            number = int(input("Number: "))
            number -= 1
            players.DeletePlayer(number)
            print()
            continue
            
        if UserVariable == 4:
            players.MovePlayer()
            print()
            continue
            
        elif UserVariable == 5:
            players.EditPlayerPosition()
            print()
            continue

        elif UserVariable == 6:
            players.EditPlayer()
            print()
            continue          

        elif UserVariable == 7:
            print("Bye!")
            #write(players) currently can't update file because Lineup isn't iterable yet
            break
        
        elif UserVariable < 1 or UserVariable > 7:
            print("Not a valid option. Please try again.")
            continue

if __name__ == "__main__":
    main()
    
