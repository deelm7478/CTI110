# A program that draws both a square and a triangle
# 10/23/18
# CTI-110 P4T1a: Shapes
# Mathew Deel
#

#Import function
import turtle

#Specify shapes and playground
win = turtle.Screen()
s = turtle.Turtle()
t = turtle.Turtle()

#Specify pen characteristics for triangle
t.pensize(3)            
t.pencolor("green")     
t.shape("turtle")

#Specify pen characteristics for square
s.pensize(2)            
s.pencolor("red")     
s.shape("square")

#Draws triangle
for draw in range(3):
    t.forward(50)
    t.left(120)

#Moves pen to new spot
s.penup()
s.forward(70)
s.pendown()

#Draws square
for draw in range(4):
    s.forward(50)
    s.left(90)

# end commands
win.mainloop()
