# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window=Tk()
    window.withdraw
    radius= simpledialog.askinteger("Circle Calculator", "Enter a number for the radius for your circle")
    pi=math.pi
    area=pi*radius*radius
    circumference=pi*2*radius
    choose=simpledialog.askstring("Circle Calculator", "Would you like to see the area or the circumference of the circle")
    if choose.lower()=="area":
        messagebox.showinfo("Circle Calculator", area)
    elif choose.lower()=="circumference":
        messagebox.showinfo("Circle Calculator", circumference)
#Area = πr^2
#Circumference = 2πr 