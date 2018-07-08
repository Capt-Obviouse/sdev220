'''
Jesse Duncan
SDEV 220
Programming Exercise: 6.4
Due June 17, 2018
'''
def main():
    number = eval(input("Enter an integer: "))
    reverse(number)

def reverse(number):
    while number != 0:
        remainder = number % 10
        print(remainder, end = "")
        number = number // 10
    print("")

main()
