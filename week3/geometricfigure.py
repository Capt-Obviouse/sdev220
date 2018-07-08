'''
Jesse Duncan
SDEV 220
Programming Assignment: 9.3
Due June 24, 2018
'''

from tkinter import *



class MainGUI:
    def __init__(self):

        self.fill = False # Default to no fill
        self.width = 500 # Width of canvas
        self.height = 200 # Heigh of canvas
        window = Tk() # Create a window
        window.title("Radiobuttons and Checkbuttons") # Set a title

        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()
        self.displayRectangle() # Default display of rectangle
        frame = Frame(window)
        frame.pack()
        self.v1 = StringVar()
        self.v1.set("R")
        rectangleShape = Radiobutton(frame, text = "Rectangle", variable = self.v1, value = "R", command = self.processRadioButton)
        ovalShape = Radiobutton(frame, text = "Oval", variable = self.v1, value = "O", command = self.processRadioButton)
        rectangleShape.grid(row = 1, column = 1)
        ovalShape.grid(row = 1, column = 2)
        self.v2 = IntVar()
        checkButton1 = Checkbutton(frame, text = "Filled", variable = self.v2, command = self.processCheckButton)
        checkButton1.grid(row = 1, column = 3)



        window.mainloop() # Create an event loop

    def displayRectangle(self): # Will display a rectangle
        fill = self.getFill();
        self.canvas.delete("all")
        if fill == True:
            self.canvas.create_rectangle(50, 25, self.width-50, self.height-50, fill = "red")
        else:
            self.canvas.create_rectangle(50, 25, self.width-50, self.height-50)

    def displayOval(self): # Will display an oval
        self.canvas.delete("all")
        fill = self.getFill();
        if fill == True:
            self.canvas.create_oval(50, 10, self.width-50, self.height-50, fill = "red")
        else:
            self.canvas.create_oval(50, 10, self.width-50, self.height-50)

    def getFill(self): # Get method for fill
        return self.fill

    def setFill(self, fill): # Set method for fill
        self.fill = fill

    def processRadioButton(self): # Handles radio button changes for shapes
        if self.v1.get() == "R":
            self.displayRectangle()
        elif self.v1.get() == "O":
            self.displayOval()

    def processCheckButton(self): # Handles checkbox changes for filled
        if self.v2.get() == 1:
            self.setFill(True)
        elif self.v2.get() == 0:
            self.setFill(False)
        if self.v1.get() == "R":
            self.displayRectangle()
        elif self.v1.get() == "O":
            self.displayOval()



MainGUI()
