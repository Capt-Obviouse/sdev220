'''
Jesse Duncan
SDEV 220
Exam 1: Part 2 - Exercise 11.11
Due July 1, 2018
'''


def displayHeadsTails(number): # Convert a number into binary
    binaryNumber = '{0:09b}'.format(number)
    binaryNumbersList = list(str(binaryNumber))
    binaryList = [] # Init a blank list to store the H & T
    for x in binaryNumbersList:
        coinSide = "N"
        if x == "0":
            coinSide = "H"
        else:
            coinSide = "T"
        binaryList.append(coinSide)
    start = 0 # Starting position to track when to insert line break
    for x in binaryList:
        if(start == 3 or start == 6): # Inserts line break after 3 characters
            print("\n", end = "")
        print(x, end = " ")
        start += 1
    print("\n")
userInput = eval(input("Enter a number between 0 and 511: "))
displayHeadsTails(userInput)
