'''
Jesse Duncan
SDEV 220
Programming Assignment: 7.7
Due June 17, 2018
'''

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a, self.b, self.c, self.d, self.e, self.f = a, b, c, d, e, f
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.d
    def getE(self):
        return self.e
    def getF(self):
        return self.f
    def isSolvable(self):
        if (self.getA() * self.getD()) - (self.getB() * self.getC()) != 0:
            return True
        else:
            print("The equation has no solution")
    def getX(self):
        if self.isSolvable():
            x = ((self.getE() * self.getD()) - (self.getB() * self.getF())) / ((self.getA() * self.getD()) - (self.getB() * self.getC()))
            return x
    def getY(self):
        if self.isSolvable():
            y = ((self.getA() * self.getF()) - (self.getE() * self.getC())) / ((self.getA() * self.getD()) - (self.getB() * self.getC()))
            return y

userInput = eval(input("Enter a, b, c, d, e, f: "))

a = userInput[0]
b = userInput[1]
c = userInput[2]
d = userInput[3]
e = userInput[4]
f = userInput[5]

myEquation = LinearEquation(a, b, c, d, e, f)
if myEquation.isSolvable():
    print("x is", myEquation.getX())
    print("y is", myEquation.getY())
