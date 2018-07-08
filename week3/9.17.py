'''
Jesse Duncan
SDEV 220
Programming Assignment: 9.17
Due June 24, 2018
'''
from tkinter import * # Import tkinter

width = 400
height = 200
radius = 80

class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Racing Car") # Set a title

        self.canvas = Canvas(window, bg = "white", width = width, height = height)
        self.canvas.pack()
        self.moveForward = 2
        self.displayCar()
        #self.canvas.move("car", self.moveForward, 0)
        self.canvas.bind("<Up>", self.processKeyEvent)
        self.canvas.bind("<Down>", self.processKeyEvent)
        self.canvas.focus_set()
        x = 0 # starting position
        while True:
            self.canvas.move("car", self.moveForward, 0)
            self.canvas.after(100)
            self.canvas.update()
            if x < width:
                x += self.moveForward
            else:
                x = 0
                self.canvas.delete("all")
                self.displayCar()

        window.mainloop() # Create an event loop

    def displayCar(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(20, 170, 30, 190, tags = "car", fill = "black", outline = "")
        self.canvas.create_polygon(0, 190, 20, 170, 20, 190, tags = "car", fill = "black", outline = "")
        self.canvas.create_polygon(50, 190, 29, 170, 30, 190, tags = "car", fill = "black", outline = "")
        self.canvas.create_rectangle(0, 180, 50, 190, tags = "car", fill = "red")
        self.canvas.create_oval(10, 190, 20, 200, tags = "car", fill = "black")
        self.canvas.create_oval(30, 190, 40, 200, tags = "car", fill = "black")

    def processKeyEvent(self, event):
        if event.keysym == "Up":
            self.moveForward += 1
        elif event.keysym == "Down":
            if self.moveForward > 0:
                self.moveForward -= 1


MainGUI()
