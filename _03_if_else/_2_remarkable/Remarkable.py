from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    name=simpledialog.askstring("Remarkable", "Pick a name out of Sarika, Dana, and David.")
    if name.lower()=="sarika":
        messagebox.showinfo("Remarkable", "Sarika is a good person.")
    elif name.lower()=="dana":
        messagebox.showinfo("Remarkable", "Dana is a good coder.")
    elif name.lower()=="david":
        messagebox.showinfo("Remarkabke", "David is good at coding shapes.")
    elif name.lower()=="daniel":
        messagebox.showinfo("Remarkable", "Daniel is a nice person.")
    else:
        messagebox.showinfo("Remarkable", "I have no idea who you are so you get no compliment.")