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
getInput = eval(input("Enter an account id: "))

for x in accountList:
    print(str(x.getId()))


validInput = False
while validInput == False:
    for x in accountList:
        if x.getId() == getInput:
            validInput = True
            break
    getInput = eval(input(("The ID you entered is incorrect, please enter an account id: ")))
