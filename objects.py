"""
contains Player and Lineup classes for the Baseball Case Study
Player will contain all the variables for each player
Lineup contains all the Player objects and all the edits you need to do with them
"""


class Player():
    def __init__(self, FirstName, LastName, Position, AtBats, Hits):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Position = Position
        self.AtBats =  AtBats
        self.Hits = Hits
        
class Lineup():
    def __init__(self,Player):
        self.__list = Player

    def __str__(self):
       return str(self.__list)

    def __itr__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list)-1:
            raise StopIteration()
        self.__index += 1
        player = self.__list[self.__index]
        return player

    def AddPlayer(self,FirstName,LastName,Position,AtBats,Hits):
        player = Player(FirstName,LastName,Position,AtBats,Hits)
        self.__list.append(player)
        print(FirstName + " " + LastName + " " + " was added.")
        print()

    def DeletePlayer(self,number):
        player = self.__list[number]
        print(player.FirstName + " was removed.")
        self.__list = self.__list.pop(number)

    def MovePlayer(self):
        CurrentLineup = int(input("Current lineup number: "))
        CurrentLineup -= 1
        name = self.__list[CurrentLineup].FirstName
        AB = self.__list[CurrentLineup].AtBats
        H = self.__list[CurrentLineup].Hits
        print("You selected", name, "AB=" + str(AB), "H=" + str(H)) 
        player = self.__list[CurrentLineup]
        self.__list.pop(CurrentLineup)
        NewLineup = int(input("New lineup number: "))
        NewLineup -= 1
        self.__list.insert(NewLineup, player)

    def  EditPlayer(self):
        player = []
        NewLineup = int(input("Lineup Number: "))-1
        name = self.__list[NewLineup].FirstName
        AB = self.__list[NewLineup].AtBats
        H = self.__list[NewLineup].Hits
        print("You selected", name, "AB=" + str(AB), "H=" + str(H))
        AB = int(input("At bats: "))
        H = int(input("Hits: "))
        self.__list[NewLineup].AtBats = AB
        self.__list[NewLineup].Hits = H
        print(name, "was updated.")

    def EditPlayerPosition(self):
        number = int(input("Number: "))
        number -= 1
        position = str(input("New Position: "))
        self.__list[number].Position = position
        
        
       

