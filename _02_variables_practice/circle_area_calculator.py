import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius= simpledialog.askinteger("Circle", "What radius would you like for your circle")
    
    # Make a new turtle
    turt=turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    turt.circle()
    # Call the turtle .penup() method
    turt.penup()
    # Move your turtle to a new x,y position using .goto()
    turt.goto(235, 345)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    pi=math.pi
    area=pi * radius * radius
    # Write the area of your circle using the turtle .write() method
    # myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle

    # Call turtle.done()

    window.mainloop()