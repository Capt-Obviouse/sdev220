'''
Jesse Duncan
SDEV 220
Programming Exercise: 6.2
Due June 17, 2018
'''
def main():
    value = eval(input("Enter a number: "))

    print("The sum of digits for " + str(value) + " is " + str(sumDigits(value)))

def sumDigits(n):
    temp = abs(n)
    sum = 0

    while temp != 0:
        remainder = temp % 10
        sum += remainder
        temp = temp // 10

    return sum

main()
