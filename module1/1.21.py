'''
Jesse Duncan
SDEV 220
Turtle: Display a clock
Due June 10, 2018
'''
import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
# Create the clock face and hands
turtle.circle(100)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(0, 55)
turtle.goto(0, 0)
turtle.goto(55, 0)
turtle.goto(-55, 0)
turtle.penup()
turtle.goto(-4, 85)
# Write the text to the clock
turtle.write("12")
turtle.goto(0, -95)
turtle.write("6")
turtle.goto(-10, -115)
turtle.write("9:15:00")
turtle.goto(-85, -3)
turtle.write("9")
turtle.goto(85, -3)
turtle.write("3")
turtle.hideturtle()
turtle.done()
