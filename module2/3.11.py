'''
Jesse Duncan
SDEV 220
Exercise 3.11
Due June 10, 2018
'''
# get user input
userInput = eval(input("Enter an integer: "))
# Convert to string and use slice to reverse the order
userInput = str(userInput)[::-1]
# display string in reversed order
print("The reversed number is " + userInput)
