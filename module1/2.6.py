'''
Jesse Duncan
SDEV 220
Chapter 2
Due June 10, 2018
'''
# Get Users input
userInput = eval(input("Enter a number between  0 and 1000: "))
# Get the last digit
lastDigit = userInput % 10
# Remove Last digit
removeDigit = userInput // 10
# Get the second to last digit
secondToLastDigit = removeDigit % 10
# remove the second to last digit
removeDigit = removeDigit // 10
# get the third to last number
thirdToLastDigit = removeDigit % 10

# Calculate the sum of the digits
calculateSum = lastDigit + secondToLastDigit + thirdToLastDigit

# Display the sum
print("The sum of the digits is " + str(calculateSum))
