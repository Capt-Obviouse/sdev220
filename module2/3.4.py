'''
Jesse Duncan
SDEV 220
Exercise 3.4
Due June 10, 2018
'''
import math

side = eval(input("Enter the side: "))

area = (5 * (side * side)) / (4 * math.tan(math.pi / 5))

print("The area of the pentagon is " + str(area))
