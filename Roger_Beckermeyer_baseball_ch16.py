############################################
# Class: CPTR 226 - Computer Science I
# Assignment: Case Study ch11
# Author(s): Lee
# Date: 11/10/19
############################################

#imports
from CaseStudyModule import *
from CaseStudyModule_ReadAndWrite import *
from CaseStudyModule_PlayerClass import Player,Lineup



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
            players = players.AddPlayer(FirstName,LastName,Position,AtBats,Hits)
            continue
            
        elif UserVariable == 3:
            number = int(input("Number: "))
            number -= 1
            players.DeletePlayer(number)
            #write(players) currently can't update file because Lineup isn't iterable yet
            continue
            
        if UserVariable == 4:
            CurrentLineup = int(input("Current lineup number: "))
            CurrentLineup -= 1
            name = players[CurrentLineup].FirstName
            AB = players[CurrentLineup].AtBats
            H = players[CurrentLineup].Hits
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
            number -= 1
            position = str(input("New Position: "))
            players[number].Position = position
            write(players)
            print()
            continue

        elif UserVariable == 6:
            player = []
            NewLineup = int(input("Lineup Number: "))-1
            name = players[NewLineup].FirstName
            AB = players[NewLineup].AtBats
            H = players[NewLineup].Hits
            print("You selected", name, "AB=" + str(AB), "H=" + str(H))
            AB = int(input("At bats: "))
            H = int(input("Hits: "))
            player = players[NewLineup]
            player.AtBats = AB
            player.Hits = H
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
    
