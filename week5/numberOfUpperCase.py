'''
Jesse Duncan
SDEV 220
Programming Assignment: Numbef of Upper Case - 15.13
Due July 8, 2018
'''

def main():
    userInput = input("Enter a string: ")
    print("The number of uppercase letters is: ", countUpperCase(userInput))

def countUpperCase(s):
    return countUpperCaseHelper(s, 0)

def countUpperCaseHelper(s, high):
    if not s:
            return high
    else:
        if s[0].isupper():
            high += 1
        return countUpperCaseHelper(s[1:], high)
main()
