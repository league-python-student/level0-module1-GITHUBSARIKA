# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw
    numOne = simpledialog.askinteger("Calculator", "Enter a number")
    numTwo = simpledialog.askinteger("Calculator", "Enter another number")
    choice=simpledialog.askstring("Calculator", "Would you like to add, subtract, multiply, or divide these variables?")
    if choice.lower()=="add":
        messagebox.showinfo("Calculator", numOne+numTwo)
    if choice.lower()=="subtract":
        messagebox.showinfo("Calculator", numOne-numTwo)
    if choice.lower()=="multiply":
        messagebox.showinfo("Calculator", numOne*numTwo)
    if choice.lower()=="divide":
        messagebox.showinfo("Calculator",numOne/numTwo)