'''
Jesse Duncan
SDEV 220
Programming Assignment: Replace Text - 13.5
Due July 8, 2018
'''
import os

def replaceText(fileName, oldString, newString):
    with open(fileName) as f:
        s = f.read()
        if oldString not in s:
            return
    with open(fileName, 'w') as f:
        s = s.replace(oldString, newString)
        f.write(s)

while True: # Loop until a valid filename
    fileName = input("Enter a filename: ")
    if os.path.isfile(fileName):
        infile = open(fileName, "r")
        infileContents = infile.readlines()
        infile.close()
        oldString = input("Enter the old string to be replaced: ")
        newString = input("Enter the new string to replace the old string: ")

        replaceText(fileName, oldString, newString)

        print("Done")
        break
    else:
        print("File does not exist")
