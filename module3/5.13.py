'''
Jesse Duncan
SDEV 220
Programming Assignment: 5.13
Due June 17, 2018
'''

printCount = 0

for count in range(100, 1001):
    if(printCount == 10):
        print("\n")
        printCount = 0
    if (count % 5) == 0 and (count % 6) > 0:
            print(count, end = ' ')
            printCount += 1
    else:
        if (count % 6) == 0:
            print(count, end = ' ')
            printCount += 1

    count += 1


print("")
