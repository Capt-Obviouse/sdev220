'''
Jesse Duncan
SDEV 220
Programming Exercise: 10.2
Due June 24, 2018
'''

def main():
    # Read numbers as a string from the console
    s = input("Enter numbers separated by spaces from one line: ")
    items = s.split() # Extracts items from the string
    numbers = [ eval(x) for x in items ] # Convert items to numbers
    numbers.reverse()
    print(numbers)

main()
