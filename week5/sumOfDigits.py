'''
Jesse Duncan
SDEV 220
Programming Assignment: Sum of Digits - 15.1
Due July 8, 2018
'''

def main():
    userInput = eval(input("Enter an integer"))
    print("The sum of the digits is", sumDigits(userInput))

def sumDigits(number):
    if number == 0:
        return 0
    else:
        return (number%10) + sumDigits(number//10)
main()
