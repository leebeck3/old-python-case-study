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
        
