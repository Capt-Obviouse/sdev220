'''
Jesse Duncan
SDEV 220
Programming Exercise: 11.2
Due July 1, 2018
'''

def main():
    matrix = []

    for i in range(4):
        s = input("Enter a 4-by-4 matrix row " + str(i) + ": ")
        items = s.split() # Extracts items from the string
        list = [ eval(x) for x in items ] # Convert items to numbers
        matrix.append(list)

    print("Sum of the elements in the major diagonal is "
            + str(sumMajorDiagonal(matrix)))

def sumMajorDiagonal(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]
    return sum

main()
