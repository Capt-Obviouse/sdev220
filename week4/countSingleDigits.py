'''
Jesse Duncan
SDEV 220
Exam 1: Part 2 - Exercise 10.7
Due July 1, 2018
'''
import random

counts = [] # List to hold the count of numbers
for x in range(10): # Loop to build the List
    counts.append(0)
for x in range(1000): # Loop 1000 times to generate numbers
    randnum = random.randint(0,9)
    print(randnum)
    counts[randnum] += 1

positionCount = 0 # Track the position in the list
print("Numbef of each integer")
for x in counts:
    print(str(positionCount) + ":", str(x))
    positionCount += 1
