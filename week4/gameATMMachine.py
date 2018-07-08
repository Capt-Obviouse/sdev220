'''
Jesse Duncan
SDEV 220
Programming Assignment: Game ATM Machine 12.3
Due July 1, 2018
'''
class Account:
    def __init__(self):
        self.id = 0
        self.balance, self.annualInterestRate = 100.00, 0.00
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
    def getBalance(self):
        return self.balance
    def setBalance(self, balance):
        self.balance = balance
    def getAnnualInterestRate(self):
        return self.annualInterestRate
    def setAnnualInterestRate(self, rate):
        self.annualInterestRate = rate
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12 / 100
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount


idList = 0
accountList = []
while idList <= 9:
    accountList.append(Account())
    accountList[idList].setId(idList)
    idList += 1

while True: # Main game loop

    getAccountID = eval(input("Enter an account id: "))

    validInput = False
    while validInput == False:
        for x in accountList:
            if x.getId() == getAccountID:
                validInput = True
                break
        if validInput == False:
            getAccountID = eval(input(("The ID you entered is incorrect, please enter an account id: ")))
    # Individual account menu loop
    exit = False
    while exit == False:
        getInput = eval(input("\n" + "Main Menu" + "\n" + "1: check balance " + "\n" + "2: withdraw " + "\n" + "3: deposit " + "\n" + "4: exit " + "\n" + "Enter a choice: "))
        if getInput == 1:
            print("The balance is: ", accountList[getAccountID].getBalance())
        elif getInput == 2:
            withdrawAmount = eval(input("Enter an amount to withdraw: "))
            accountList[getAccountID].withdraw(withdrawAmount)
        elif getInput == 3:
            depositAmount = eval(input("Enter an amount to deposit: "))
            accountList[getAccountID].deposit(depositAmount)
        elif getInput == 4:
            exit = True
        else:
            print("Invalid Entry, please try again")
