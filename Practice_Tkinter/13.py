from tkinter import *
import tkinter.messagebox

root = Tk()

canvas = Canvas(root, width=200, height= 200)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50) #starting pt, ending pt 
redLine = canvas.create_line(0, 100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")

canvas.delete(redLine)
canvas.delete(ALL)


root.mainloop()