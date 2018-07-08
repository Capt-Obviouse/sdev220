'''
Jesse Duncan
SDEV 220
Programming Exercise: 13.2
Due July 8, 2018
'''

def main():
    # Prompt the user to enter filenames
    f1 = input("Enter a filename: ").strip()

    # Open files for input
    infile = open(f1, "r")

    s = infile.read() # Read all from the file

    print(str(len(s)) + " characters")
    print(str(len(s.split())) + " words")
    print(str(len(s.split('\n'))) + " lines")

    infile.close() # Close the output file

main()
