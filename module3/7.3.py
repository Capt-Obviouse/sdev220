'''
Jesse Duncan
SDEV 220
Programming Assignment: 7.3
Due June 17, 2018
'''

class Account:
    def __init__(self):
        self.id = 0
        self.balance, self.annualInterestRate = 100.00, 0.00
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id
        print("ID set to: " + str(id))
    def getBalance(self):
        return self.balance
    def setBalance(self, balance):
        self.balance = balance
        print("Balance set to: " + str(balance))
    def getAnnualInterestRate(self):
        return self.annualInterestRate
    def setAnnualInterestRate(self, rate):
        self.annualInterestRate = rate
        print("Annual Interest Rate set to: " + str(rate))
    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12 / 100
    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()
    def withdraw(self, amount):
        self.balance -= amount
        print(str(amount) + " has been withdrawn")
    def deposit(self, amount):
        self.balance += amount
        print(str(amount) + " has been deposited")
newAccount = Account()
newAccount.setId(1122)
newAccount.setBalance(20000)
newAccount.setAnnualInterestRate(4.5)
newAccount.withdraw(2500)
newAccount.deposit(3000)
print("ID:", newAccount.getId())
print("Balance:", newAccount.getBalance())
print("Monthly Interest Rate:", newAccount.getMonthlyInterestRate())
print("Monthly Interest:", newAccount.getMonthlyInterest())
