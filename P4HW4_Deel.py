# A program that draws a shape using a nested loop
# 10/23/18
# CTI-110 P4HW4: Nested Loops
# Mathew Deel
#

def main():
    #Import function
    import turtle

    #Specify shapes and playground
    win = turtle.Screen()
    shape = turtle.Turtle()

    #Specify pen characteristics
    shape.pensize(3)            
    shape.pencolor("blue")
    shape.speed(10)

    #Position pen
    shape.penup()
    shape.right(90)
    shape.forward(200)
    shape.left(90)
    shape.pendown()

    #Start nested drawing loop
    for penta in range(10):
        for square in range(4):
            shape.forward(100)
            shape.right(90)
        shape.forward(100)
        shape.left(36)
            
    # end commands
    win.mainloop()

main()
