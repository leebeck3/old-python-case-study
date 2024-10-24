############################################
# Class: CPTR 226 - Computer Science I
# Assignment: Case Study ch5
# Author(s): Lee
# Date: 10/6/19
############################################

#menu function
 print("================================================================================")
    print("      Baseball Team Manager        ")
    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")
    print("================================================================================")

#error checker for AtBats and Hits
def ErrorCheckerAndAverage():
    #error checker variables
            counter = 0
            
            #error checker loop
            while counter <= 1:
                
                #user input
                OfficialAtBats = int(input("Official number of at bats: "))
                NumberOfHits = int(input("Number of hits: "))
                counter += 1
                
                #error checker
                if NumberOfHits > OfficialAtBats:
                    print("Error, official at bats can't be greater than number of hits please try again.")
                    print()
                    counter -= 1
                    continue
                elif NumberOfHits < 0:
                    print("Error, Can't have negative number of hits, please try again.")
                    print()
                    counter -= 1
                    continue
                elif OfficialAtBats < 1:
                    print("Error, official times at bat can't be less than 1, please try again.")
                    print()
                    counter -= 1
                    continue
                else:
                    counter += 1
                    break
                
            #average calculator
            BattingAverage = battingaverage(NumberOfHits, OfficialAtBats)
            return BattingAverage



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
            BattingAverage = ErrorCheckerAndAverage()
                
            #return batting average
            print("Batting average: " + BattingAverage)
            print()
            continue
            

        
        #program exit
        if UserVariable == 7:
            print("Bye!")
            break
        
        #error check
        else:
            print("Not a valid option. Please try again.")
            continue

if __name__ == "__main__":
    main()
    
