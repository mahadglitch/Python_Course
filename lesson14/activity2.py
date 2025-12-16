import tkinter as tik

window = tik.Tk()

for i in range(4): # rows
    for j in range(4): # columns
        frame = tik.Frame(
            master=window,
            relief=tik.RAISED,
            borderwidth=8
        )
        frame.grid(row=i,column=j,padx=10,pady=10) # padding in x-axis and padding in y-axis
        label = tik.Label(master=frame,text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()        