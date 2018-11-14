import sys
from tkinter import * 

root = Tk()

one = Label(root, text='One', bg="red", fg="white")
one.pack()
two = Label(root, text='Two', bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text='Two', bg="green", fg="black")
two.pack(fill=X)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()