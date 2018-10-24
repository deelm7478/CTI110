# A program that draws a snowflake.
# 10/23/18
# CTI-110 P4T1c: Initials
# Mathew Deel
#

#Import function
import turtle

#Specify shapes and playground
win = turtle.Screen()
snowflake = turtle.Turtle()

#Specify pen characteristics
snowflake.pensize(3)            
snowflake.pencolor("blue")
snowflake.speed(4)

#Start drawing
snowflake.right(90)

for snow in range(6):
    snowflake.forward(100)
    snowflake.forward(-40)
    snowflake.left(40)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.right(80)
    snowflake.forward(35)
    snowflake.forward(-35)
    snowflake.left(40)
    snowflake.forward(-60)
    snowflake.left(60)
    
# end commands
win.mainloop()
