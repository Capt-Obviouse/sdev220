'''
Jesse Duncan
SDEV 220
Programming Assignment: The Triangle 12.1
Due July 1, 2018
'''
import math

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color
    def isFilled(self):
        if self.__filled == 1:
            return True
        else:
            return False
    def setFilled(self, filled):
        self.__filled = filled
    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self):
        self.side1 = self.side2 = self.side3 = 1.0
    def getSide1(self):
        return self.side1
    def getSide2(self):
        return self.side2
    def getSide3(self):
        return self.side3
    def setSide1(self, side):
        self.side1 = side
    def setSide2(self, side):
        self.side2 = side
    def setSide3(self, side):
        self.side3 = side
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3)/2
        area = s * (s - self.side1)*(s - self.side2)*(s - self.side3)
        area = math.sqrt(area)
        return area
    def getPerimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter
    def __str__():
        return "Triangle: side1 = " + str(side1) + " side2 = " + str(side2) + " side3 = " + str(side3)
t = Triangle()
side1, side2, side3 = eval(input("Please enter three sides of a triangle seperated by commas: "))
t.setSide1(side1)
t.setSide2(side2)
t.setSide3(side3)

userColor = input("Please enter a color for the triangle: ")
t.setColor(userColor)

userFill = eval(input("Please indicate if the triangle is filled 1 being filled 0 being empty: "))
t.setFilled(userFill)

print(" Area:", str(t.getArea()), "\n", "Perimeter:", str(t.getPerimeter()), "\n", "Color:", t.getColor(), "\n", "Filled:", str(t.isFilled()))
