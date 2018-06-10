'''
Jesse Duncan
SDEV 220
Exercise 3.14
Due June 10, 2018
'''
import turtle

# Get the users input for circle radius (50 is optimal)
radius = eval(input("Enter the radius for the circles: "))

turtle.pensize(5)

# Draw blue ricle
turtle.color("blue")
turtle.penup()
turtle.goto(-110, -25)
turtle.pendown()
turtle.circle(radius)

# Draw black circle
turtle.color("black")
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.circle(radius)

# Draw red circle
turtle.color("red")
turtle.penup()
turtle.goto(110, -25)
turtle.pendown()
turtle.circle(radius)

# Draw yellow circle
turtle.color("yellow")
turtle.penup()
turtle.goto(-55, -75)
turtle.pendown()
turtle.circle(radius)

# Draw green circle
turtle.color("green")
turtle.penup()
turtle.goto(55, -75)
turtle.pendown()
turtle.circle(radius)

turtle.hideturtle()

turtle.done()
