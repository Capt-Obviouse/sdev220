'''
Jesse Duncan
SDEV 220
Programming Assignment: 11.9
Due June 24, 2018
'''
class Game():
    def __init__(self):
        self.turns = 9
        self.player = "X"
        self.gameList = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        while self.turns > 0:
            self.displayGameBoard()
            self.getUserInput()
            if self.checkForWinner():
                break
            self.turns -= 1
            self.displayGameBoard()
            print("Draw! Try again.")

    def displayGameBoard(self):
        print("-------------------")
        print ("|  " + self.gameList[0][0] + "  |  " + self.gameList[0][1] + "  |  " + self.gameList[0][2] + "  |")
        print("-------------------")
        print ("|  " + self.gameList[1][0] + "  |  " + self.gameList[1][1] + "  |  " + self.gameList[1][2] + "  |")
        print("-------------------")
        print ("|  " + self.gameList[2][0] + "  |  " + self.gameList[2][1] + "  |  " + self.gameList[2][2] + "  |")
        print("-------------------")

    def checkForWinner(self):
        # Check for diagonal wins
        if self.gameList[0][0] == self.gameList[1][1] == self.gameList[2][2]:
            if self.gameList[0][0] != " ":
                self.displayGameBoard()
                print(self.gameList[0][0], "player won")
                return True
        if self.gameList[2][0] == self.gameList[1][1] == self.gameList[0][2]:
            if self.gameList[2][0] != " ":
                self.displayGameBoard()
                print(self.gameList[2][0], "player won")
                return True

        # Check for row wins
        for row in self.gameList:
            xCount = 0
            oCount = 0
            for value in row:
                if value == "X":
                    xCount += 1
                elif value == "O":
                    oCount += 1
                if xCount == 3:
                    self.displayGameBoard()
                    print("X player won")
                    return True
                elif oCount == 3:
                    self.displayGameBoard()
                    print("O player won")
                    return True

        # Check for column wins
        for column in range(len(self.gameList[0])):
            xCount = 0
            oCount = 0
            for row in range(len(self.gameList)):
                if self.gameList[row][column] == "X":
                    xCount += 1
                elif self.gameList[row][column] == "O":
                    oCount += 1
                if xCount == 3:
                    self.displayGameBoard()
                    print("X player won")
                    return True
                elif oCount == 3:
                    self.displayGameBoard()
                    print("O player won")
                    return True

    def getUserInput(self):
        if self.turns % 2 == 0:
            self.player = "O"
        else:
            self.player = "X"
        validInput = False
        while validInput == False:
            userInputRow = eval(input("Enter a row (0, 1, or 2) for player " + self.player + ": "))
            userInputColumn = eval(input("Enter a columns (0, 1, or 2) for player " + self.player + ": "))
            if self.gameList[userInputRow][userInputColumn] == " ":
                self.gameList[userInputRow][userInputColumn] = self.player
                validInput = True
            else:
                print("Space is already selected please try again")


Game()
