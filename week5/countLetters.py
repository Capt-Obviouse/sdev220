'''
Jesse Duncan
SDEV 220
Programming Assignment: Count Letters - 14.5
Due July 8, 2018
'''

from tkinter import * # Import tkinter
import tkinter.messagebox # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename
width = 500
height = 200
radius = 2
bottomGap = 10
def showResult():
    analyzeFile(filename.get())

def analyzeFile(filename):
    try:
        infile = open(filename, "r") # Open the file

        counts = 26 * [0] # Create and initialize counts
        for line in infile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)
        barWidth = (width - 20) / len(counts)
        maxCount = int(max(counts))
        # Display results
        canvas.delete("all")
        for i in range(len(counts)):
            canvas.create_rectangle(i * barWidth + 10, (height - bottomGap - 10) * (1 - counts[i] / (maxCount + 4)),
                (i + 1) * barWidth + 10, height - bottomGap - 10, tag = "line")
            canvas.create_text((i + 1) * barWidth + 5, height - bottomGap, text = chr(ord('a') + i))

        infile.close() # Close file
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                    "File " + filename + " does not exist")

# Count each letter in the string
def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)

window = Tk() # Create a window
window.title("Occurrence of Letters Histogram") # Set title
frame1 = Frame(window)
frame1.pack(fill = BOTH, expand = True)
canvas = Canvas(frame1, width = width, height = height)
canvas.pack(side = LEFT, fill = BOTH, expand = True)

frame2 = Frame(window) # Hold four labels for displaying cards
frame2.pack()


Label(frame2, text = "Enter a filename: ").pack(side = LEFT)
filename = StringVar()
Entry(frame2, width = 20, textvariable = filename).pack(side = LEFT)
Button(frame2, text = "Browse", command = openFile).pack(side = LEFT)
Button(frame2, text = "Show Result", command = showResult).pack(side = LEFT)
window.mainloop() # Create an event loop
