from tkinter import messagebox, simpledialog, Tk

#Write a python program that asks the user a minimum of 3 riddles.
if __name__ == '__main__':
    window=Tk()
    window.withdraw()
    score=0
    riddleOne=simpledialog.askinteger("Riddles", "Mr. and Mrs. Mustard have six daughters and each daughter has one brother. How many people are in the Mustard family?")
    if riddleOne==9:
        score+=1
    riddletwo=simpledialog.askstring("Riddles", "What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? What is it?")
    if riddletwo.lower()=="dice":
        score+=1
    riddlethree=simpledialog.askstring("Riddles","I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")
    if riddlethree.lower()=="fire":
        score+=1
    messagebox.showinfo("Riddles", "You got " + str(score) + " answers correct!")
# You can look at riddles.com if you don't already know any riddles.

# Collect the response of each riddle from the user and compare their
  #answers to the correct answer.

# Use a variable to keep track of the correctly answered riddles

# After all the riddles have been asked, tell the user how many they got correct
