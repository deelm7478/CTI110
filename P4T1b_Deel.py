# A program that draws both my first and last initials.
# 10/23/18
# CTI-110 P4T1b: Initials
# Mathew Deel
#

#Import function
import turtle

#Specify shapes and playground
win = turtle.Screen()
i = turtle.Turtle()

#Specify pen characteristics
i.pensize(2)            
i.pencolor("blue")

#Draws first initial
i.left(90)
i.forward(60)
i.right(155)
i.forward(65)
i.left(135)
i.forward(65)
i.right(160)
i.forward(60)

#Pen is raised and moved to new spot
i.penup()
i.left(90)
i.forward(20)
i.pendown()

#Specify characteristics of second initial
i.pencolor("red")

#Draws second initial
i.left(90)
i.forward(60)
i.right(90)
for draw in range(10):
    i.forward(11)
    i.right(20)

# end commands
win.mainloop()
