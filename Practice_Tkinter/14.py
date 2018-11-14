from tkinter import *
import tkinter.messagebox
from PIL import Image

root = Tk()
root.geometry("571x778")

photo = PhotoImage(file="NTUcampus.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()

# size = (571, 778)    
# image = Image.open("NTUcampus2.png")
# image.thumbnail(size, Image.ANTIALIAS)
# image.save("NTUcampus6" + '.png', quality=100)