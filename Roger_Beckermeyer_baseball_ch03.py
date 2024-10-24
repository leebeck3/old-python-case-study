#intro
print("================================================================================")
print("      Baseball Team Manager        ")
print()
print("MENU OPTIONS")
print("1 - Calculate batting average")
print("2 - Exit program")
print("================================================================================")

#while/if loop for menu options
while True:
    UserVariable = int(input("Menu option: "))
    if UserVariable == 1:

        #intro
        print("Calculating batting average...")

        #user input
        OfficialAtBats = int(input("Official number of at bats: "))
        NumberOfHits = int(input("Number of hits: "))
    
        #average calculator
        BattingAverage = NumberOfHits / OfficialAtBats
        BattingAverage = round(BattingAverage, 3)
        BattingAverage = str(BattingAverage)

        #return batting average
        print("Batting average: " + BattingAverage)
        print()
        continue
    #program exit
    if UserVariable == 2:
        print("Bye!")
        break
    #error check
    else:
        print("Not a valid option. Please try again.")
        print()
        continue
