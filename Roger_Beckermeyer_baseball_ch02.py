
#intro
print("================================================================================")
print("      Baseball Team Manager        ")
print()
print("This program calculates the batting average for a layer based \non the player's official number of at bats and hits.")
print("================================================================================")

#user input
PlayerName = str(input("Player's name: "))
NumberTimesAtBat = int(input("Official number of at bats: "))
NumberOfHits = int(input("Number of hits: "))

#average calculator
average = NumberOfHits / NumberTimesAtBat
average = round(average, 3)
average = str(average)

#return batting average
print(PlayerName + "'s " + "batting average is " + average)

