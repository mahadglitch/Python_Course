from tkinter import * # import necessary libraries from tkinter

window = Tk()
window.title("Tkinter Sample Window")
window.geometry("300x300")

greeting = Label(text="Hello User" , fg = 'black' , bg = 'white')
button = Button(text="Click me" , bg='black' , fg='white')
entry = Entry(fg='yellow', bg='blue' , width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window , relief=RAISED , borderwidth=5)
frame.pack()
label = Label(master=frame , text="Sample Frame")
label.pack()

textbox = Label(text = "New Window" , fg='green' , bg='yellow')
textbox.pack()
window.mainloop() # without this line , tkinter will not be visible