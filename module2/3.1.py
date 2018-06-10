'''
Jesse Duncan
SDEV 220
Exercise 3.1 Geometry: area of a pentagon
Due June 10, 2018
'''

import math

userInput = eval(input("Enter the length from the center of a pentagon to a vertex: "))

side = 2 * userInput * math.sin(math.pi/5)
area = round((3 * math.sqrt(3)/2) * (side * side), 2)

print(area)
