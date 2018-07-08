'''
Jesse Duncan
SDEV 220
Programming Assignment: 6.5
Due June 17, 2018
'''


def displaySortedNumbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()

    print("The sorted numbers are " + str(numbers[0]), str(numbers[1]), str(numbers[2]))
num1, num2, num3 = eval(input("Enter three numbers: "))

displaySortedNumbers(num1, num2, num3)
