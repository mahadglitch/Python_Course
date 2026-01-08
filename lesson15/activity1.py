#PIL (Python Imaging Library) provides image editing capability to the python interpreter
from tkinter import *
from PIL import Image, ImageTk

#PIL - pillow library

#Create a window with a title bar and set its geametry as well
root = Tk()
root.title("image")
root.geometry("800x700")
#Now use Image.open to open and identify the given image file.
upload = Image.open("image.jpg")
#Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)
#Add image to Tkinter label
label = Label(root, image=image, height=700, width=800)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add image in Tkinter window")
label2.place(x=40, y=360)

# Run the application
root.mainloop()