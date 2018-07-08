'''
Jesse Duncan
SDEV 220
Programming Assignment: 8.3
Due June 17, 2018
'''

def validatePassword(password):
    valid = True
    length = len(password)
    digitCounter = 0
    while valid:
        # Must have at least eight characters
        if length < 8: # checks if the password length is to short
            valid = False
            break
        # Must consist of only letters and digits
        for ch in password:
            if ch.isalpha(): # checks if character is a letter
                valid = True
            elif ch.isdigit(): # checks if character is a digit
                valid = True
                digitCounter += 1
            else:
                valid = False
                break
        # Must contain at least two digits
        if digitCounter < 2:
            valid = False
            break
        break
    return valid
userInput = input("Enter a password: ")

if validatePassword(userInput):
    print("valid password")
else:
    print("invalid password")
