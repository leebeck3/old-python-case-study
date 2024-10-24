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
        
       

