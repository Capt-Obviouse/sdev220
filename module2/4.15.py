'''
Jesse Duncan
SDEV 220
Exercise 4.15 Game: Lottery
Due June 10, 2018
'''
import random

# Generate a lottery number
lottery = random.randint(0, 999)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (three digits): "))

#Get digits from lottery
removeLastDigit = lottery // 10
firstDigit = removeLastDigit // 10
secondDigit = removeLastDigit % 10
thirdDigit = lottery % 10

# Get digits from guess
removeLastGuessDigit = guess // 10
guessDigit1 = removeLastGuessDigit // 10
guessDigit2 = removeLastGuessDigit % 10
guessDigit3 = guess % 10


print("The lottery number is", lottery)
if guess == lottery:
    print("Exact match: you win $10,000")
else:
    matches = 0
    # place digits into a list
    guess = [guessDigit1, guessDigit2, guessDigit3]
    lottery = [firstDigit, secondDigit, thirdDigit]

    # sort the list to be iterated
    lottery.sort()
    guess.sort()

    # if the lists match then all the digits where the same
    if lottery == guess:
        print("Match all digits: you win $3,000")
    else:
        # iterate over the list comparing each value to determine matches
        for x in lottery:
            for y in guess:
                if x == y:
                    matches += 1
                    print("match one digit: you win $1,000")
                    break
        # if no matches display sorry message
        print("Sorry, no match")
