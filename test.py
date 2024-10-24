class Dice:
    def __init__(self):
        self.__list = []

    def __iter__(self):
        self._index = 0

    def __next__(self_):
        if self.__index >= len(self.__list)-1:
            raise StopIteration()
        self.__index += 1
        die = self.__list[self.__index]
        return die

for die in Dice:
    print("ya")
