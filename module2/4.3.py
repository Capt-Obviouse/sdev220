'''
Jesse Duncan
SDEV 220
Exercise 4.3 Algebra: solve 2 x 2 linear equations
Due June 10, 2018
'''

import math

# get user input
userInput = eval(input("Enter a, b, c, d, e, f: "))

# Assign user input values to variables for the Cramer rule
a = userInput[0]
b = userInput[1]
c = userInput[2]
d = userInput[3]
e = userInput[4]
f = userInput[5]

# test if there is a no solution scenario before calculating x and y
if a * d - b *c == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", x, "and y is", y)
