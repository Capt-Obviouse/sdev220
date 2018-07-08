'''
Jesse Duncan
SDEV 220
Programming Exercise: 5.2
Due June 17, 2018
'''

import random
import time

correctCount = 0 # Count the number of correct answers
count = 0 # Count the number of questions
NUMBER_OF_QUESTIONS = 10 # Constant

startTime = time.time() # get start time

while count < NUMBER_OF_QUESTIONS:
    # Generate two random single-digit integers
    number1 = random.randint(1, 15)
    number2 = random.randint(1, 15)

    # if number1 < number2, swap number1 with number2
    if number1 < number2:
        number1, number2 = number2, number1

    # Prompt the student to answer "What is number1 - number2?"
    answer = eval(input("What is " + str(number1) + " + " + str(number2) + "? "))

    # Grade the answer and display the result
    if number1 + number2 == answer:
        print("You are correct!")
        correctCount += 1
    else:
        print("Your answer is wrong. \n", number1, "+", number2, "is", number1 + number2)

    # Increase the Count
    count += 1

endTime = time.time() # get end time
testTime = int(endTime - startTime) # Get test time
print("Correct count is", correctCount, "out of", NUMBER_OF_QUESTIONS, "\nTest time is", testTime, "seconds")
