from tkinter import simpledialog, messagebox, Tk, Canvas

windowWidth = 600
windowHeight = 600

root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices 
colorTomato=simpledialog.askstring("Tasty Tomato", "What color would you like; red, pink, or lavender")

#2. use if-else statements to draw the tomato in the color that they chose
#   you can modify the code below or draw your own tomato

if colorTomato=="red":
    canvas.create_oval(75,200, 400, 450, fill="red", outline="red" )
    canvas.create_oval(200,200, 525, 450, fill="red", outline="red" )
elif colorTomato=="pink":
    canvas.create_oval(75, 200, 400, 450, fill="pink", outline="pink")
    canvas.create_oval(200, 200, 525, 450, fill="pink", outline="pink")
elif colorTomato=="lavender":
    canvas.create_oval(200, 200, 525, 450, fill="lavender", outline="lavender")
    canvas.create_oval(75, 200, 400, 450, fill="lavender", outline="lavender")
canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="green")


root.mainloop()
