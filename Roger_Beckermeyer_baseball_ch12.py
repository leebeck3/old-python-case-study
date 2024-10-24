############################################
# Class: CPTR 226 - Computer Science I
# Assignment: Case Study ch11
# Author(s): Lee
# Date: 11/10/19
############################################

#imports
from CaseStudyModule import *


#main function
def main():
    menu()
    while True:
        players = read()
        try:
            UserVariable = int(input("Menu option: "))
        except Exception as e:
            print("Not a valid option. Please try again.")
            continue
            
        if UserVariable == 1:
            print("{:>9} {:>30} {:>7} {:>7} {:>7}".format("Player", "POS", "AB", "H", "AVG"))
            print("-" * 64)
            PlayerFormat = "{:30} {:>6} {:>7} {:>7} {:>7.2f}"
            for player in players:
                Name = players[player]["Name"]
                Position = players[player]["Position"]
                AB = players[player]["At Bats"]
                Hits = players[player]["Hits"]
                Average = players[player]["Average"]
                print(player, " ", PlayerFormat.format(Name,Position,AB,Hits,float(Average)))
            print()
            
        elif UserVariable == 2:
            name = str(input("Name: "))
            player = {}
            player["Name"] = name
            player["Position"] = (str(input("Position: ")))
            AtBats = int(input("At bats: "))
            ErrorCheckerAtBats(AtBats)
            player["At Bats"] = AtBats
            Hits = int(input("Hits: "))
            ErrorCheckerHits(AtBats,Hits)
            player["Hits"] = Hits
            Average = battingaverage(Hits, AtBats)
            player["Average"] = Average

            counter = 1
            for item in players:
                counter += 1
            
            players[counter] = player
            write(players)
            print(name, "was added.")
            print()
            continue
            
        elif UserVariable == 3:
            number = int(input("Number: "))
            print(players[number]["Name"] + " was removed.")
            players.pop(number)
            write(players)
            continue
            
        if UserVariable == 4:
            CurrentLineup = int(input("Current lineup number: "))
            name = players[CurrentLineup]["Name"]
            AB = players[CurrentLineup]["At Bats"]
            H = players[CurrentLineup]["Hits"]
            print("You selected", name, "AB=" + str(AB), "H=" + str(H)) 
            player = players[CurrentLineup]
            players.pop(CurrentLineup)
            NewLineup = int(input("New lineup number: "))
            players[NewLineup] = player
            write(players)
            print()
            continue
            
        elif UserVariable == 5:
            number = int(input("Number: "))
            position = str(input("New Position: "))
            players[number]["Position"] = position
            write(players)
            print()
            continue

        elif UserVariable == 6:
            player = {}
            Lineup = int(input("Lineup Number: "))
            name = players[Lineup]["Name"]
            AB = players[Lineup]["At Bats"]
            H = players[Lineup]["Hits"]
            print("You selected", name, "AB=" + str(AB), "H=" + str(H))
            AB = int(input("At bats: "))
            H = int(input("Hits: "))
            player = players[Lineup]
            player["At Bats"] = AB
            player["Hits"] = H
            Average = battingaverage(H, AB)
            player["Average"] = Average
            players[Lineup] = player
            write(players)
            print(name, "was updated.")
            print()
            continue          

        elif UserVariable == 7:
            print("Bye!")
            break
        
        elif UserVariable < 1 or UserVariable > 7:
            print("Not a valid option. Please try again.")
            continue

if __name__ == "__main__":
    main()
    
