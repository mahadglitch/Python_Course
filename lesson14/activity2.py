import tkinter as tik

window = tik.Tk()

for i in range(4):  # rows
    for j in range(4):  # columns
        frame = tik.Frame(
            master=window,
            relief=tik.RAIactivity3SED,
            borderwidth=8
        )
        # padding in x-axis and padding in y-axis
        frame.grid(row=i, column=j, padx=10, pady=10)
        label = tik.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()

window.mainloop()
