############################################
# Class: CPTR 226 - Computer Science I
# Assignment: Case Study ch_3
# Author(s): Lee
# Date: 9/22/19
############################################


#menu function
def menu():
    print("================================================================================")
    print("      Baseball Team Manager        ")
    print()
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")
    print("================================================================================")

#menu options to display for erros
def MenuOptions():
    print("MENU OPTIONS")
    print("1 - Calculate batting average")
    print("2 - Exit program")
    print()
    
#batting average function
def battingaverage(x,y):
    BattingAverage = x / y
    BattingAverage = round(BattingAverage, 3)
    BattingAverage = str(BattingAverage)
    return BattingAverage

#main function
def main():
    menu()
    while True:
        UserVariable = int(input("Menu option: "))
        if UserVariable == 1:

            #intro
            print("Calculating batting average...")

            #user input
            OfficialAtBats = int(input("Official number of at bats: "))
            NumberOfHits = int(input("Number of hits: "))
    
            #average calculator
            BattingAverage = battingaverage(NumberOfHits, OfficialAtBats)

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
            MenuOptions()
            continue

if __name__ == "__main__":
    main()
    
