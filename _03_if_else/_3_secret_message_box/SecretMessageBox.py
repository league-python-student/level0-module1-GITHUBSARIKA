from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    password="unicorns"
    secretMessage=simpledialog.askstring("Secret Message", "Enter in a secret message.")
    messagebox.showinfo("Secret Message", "You can only see the secret message if know the password")
    guess=simpledialog.askstring("Secret Message", "Enter the password")
    if guess=="unicorns":
        messagebox.showinfo("Secret Message", secretMessage)
    else:
        messagebox.showerror("Secret Message", "INTRUDER")