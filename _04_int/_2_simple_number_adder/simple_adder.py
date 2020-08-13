# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    numOne=simpledialog.askinteger("Simple Adder", "Enter a number")
    numTwo=simpledialog.askinteger("Simple Adder", "Enter another number")
    messagebox.showinfo("Simple Adder", numOne+numTwo)