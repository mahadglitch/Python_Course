# Import necessary libraries
from tkinter import * # importing every necessary functions insider tkinter
from tkinter import messagebox
# Setup tkinter Window
root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alart","Stop! Virus Found.")

button = Button(root, text = "Scan for Virus", command=msg)
button.place(x=70, y=20)

root.mainloop()