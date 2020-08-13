import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    turt=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring("Shape Selector", "What shape do you want to draw?")
    # Draw the shape requested by the user using if-elif-else statements
    if shape.lower()=="circle":
        turt.circle(100, steps=30)
    elif shape.lower()=="triangle":
        turt.circle(100, steps=3)
    elif shape.lower()=="square" :
        turt.circle(100, steps=4)
    else:
        turt.circle(100, steps=30)
        messagebox.showinfo("Shape Selector", "Your shape is currently available so you get a circle instead!")
    # Call the turtle .done() method
    turtle.done()
    window.mainloop()