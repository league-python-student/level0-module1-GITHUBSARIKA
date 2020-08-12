from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    birthday=simpledialog.askstring("Birthday", "What is your birthday?")
    print(birthday.lower())
    if birthday.lower() == "august 12th":
        messagebox.showinfo("Birthday", "Happy Birthday!")
    else:
        messagebox.showinfo("Birthday", "Happy unbirthday!")
    window.mainloop()