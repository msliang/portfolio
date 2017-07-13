from turtle import *
import math

# Name your Turtle.
turtle = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150

input_again=int(input ("How many shapes do you want to make? "))
for shapes in range(input_again):
    input_numSides=int(input("Enter a number of sides: "))
    for line in range(input_numSides):
        pendown()
        forward(200)
        right(360/input_numSides)
        penup()
    forward(200)



# Close window on click.
exitonclick()
