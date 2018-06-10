'''
Jesse Duncan
SDEV 220
Exercise 4.2
Due June 10, 2018
'''
import random

# Generate random numbers
number1 = random.randint(0,9)
number2 = random.randint(0,9)
number3 = random.randint(0,9)

userInput = eval(input("What is the sum of these three integers " + str(number1) + ", " + str(number2) + ", " + str(number3) + "? "))

# Check to see if the users answer is correct
validateInput = number1 + number2 + number3 == userInput

print("You entered: " + str(userInput) + ". Your answer was: " + str(validateInput))
