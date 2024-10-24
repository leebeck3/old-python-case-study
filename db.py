from CaseStudyModule_PlayerClass import *
import csv

#intakes list and imports to a .csv file
def write(x):
    with open("player_list.csv", 'w' , newline="") as file:
        writer = csv.writer(file)
        players = []
        for y in x:
            player = []
            player.append(y.FirstName)
            player.append(y.LastName)
            player.append(y.Position)
            player.append(y.AtBats)
            player.append(y.Hits)
            
            players.append(player)
        writer.writerows(players)
   
def read():
    try:
        playerlist = []
        with open("player_list.csv", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player = Player(row[0], row[1], row[2], row[3], row[4])
                playerlist.append(player)
    except:
        print()
    return playerlist
