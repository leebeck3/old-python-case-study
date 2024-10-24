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
            counter = 1
            print("{:>9} {:>30} {:>7} {:>7} {:>7}".format("Player", "POS", "AB", "H", "AVG"))
            print("-" * 64)
            PlayerFormat = "{:30} {:>6} {:>7} {:>7} {:>7.3f}"
            for player in players:
                print(str(counter) + "  " + PlayerFormat.format(player[0], player[1], player[2], player[3], float(player[4])))
                counter += 1
            print()
            
        elif UserVariable == 2:
            name = str(input("Name: "))
            player = []
            player.append(name)
            player.append(str(input("Position: ")))
            AtBats = int(input("At bats: "))
            ErrorCheckerAtBats(AtBats)
            player.append(AtBats)
            Hits = int(input("Hits: "))
            ErrorCheckerHits(AtBats,Hits)
            player.append(Hits)
            Average = battingaverage(Hits, AtBats)
            player.append(float(Average))
            players.append(player)
            write(players)
            print(name, "was added.")
            print()
            continue
            
        elif UserVariable == 3:
            number = int(input("Number: "))
            number -= 1
            print(players[number][0] + " was removed.")
            players.pop(number)
            write(players)
            continue
            
        if UserVariable == 4:
            CurrentLineup = int(input("Current lineup number: "))
            CurrentLineup -= 1
            name = players[CurrentLineup][0]
            AB = players[CurrentLineup][2]
            H = players[CurrentLineup][3]
            print("You selected", name, "AB=" + str(AB), "H=" + str(H)) 
            player = players[CurrentLineup]
            players.pop(CurrentLineup)
            NewLineup = int(input("New lineup number: "))
            NewLineup -= 1
            players.insert(NewLineup, player)
            write(players)
            print()
            continue
            
        elif UserVariable == 5:
            number = int(input("Number: "))
            position = str(input("New Position: "))
            number -= 1
            player = players[number]
            player.pop(1)
            player.insert(1,position)
            players.pop(number)
            players.insert(number, player)
            write(players)
            print()
            continue

        elif UserVariable == 6:
            Lineup = int(input("Lineup Number: "))
            Lineup -= 1
            name = players[Lineup][0]
            AB = players[Lineup][2]
            H = players[Lineup][3]
            print("You selected", name, "AB=" + str(AB), "H=" + str(H))
            AB = int(input("At bats: "))
            H = int(input("Hits: "))
            player = players[Lineup]
            player.pop(2)
            player.insert(2,AB)
            player.pop(3)
            player.insert(3,H)
            Average = battingaverage(H, AB)
            player.pop(4)
            player.insert(4,Average)
            players.pop(Lineup)
            players.insert(Lineup, player)
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
    
