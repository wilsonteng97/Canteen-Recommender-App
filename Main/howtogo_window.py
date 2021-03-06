from tkinter import *
from tkinter import ttk
from sorting_functions import count_distance


def howtogo_window(frame ,userlocate, cantlocate):
    distance = count_distance(userlocate, cantlocate)

    ##frame##
    bottomframe = Frame(frame)
    bottomframe.pack(side=BOTTOM)

    ##canvas##
    canvas = Canvas(frame)
    canvas.pack(fill=BOTH, expand=1) # Stretch canvas to root window size.

    ##image + line + circle##
    background_image= PhotoImage(file=r"Canteen-Recommender-App/Main/NTUcampus.png")
    image = canvas.create_image((0,0), anchor='nw', image=background_image)
    line = canvas.create_line( userlocate[0] ,userlocate[1], cantlocate[0],cantlocate[1], fill="red",width=3,arrow=LAST)

    frame.image = image
    circleuser = canvas.create_oval(userlocate[0]-5, userlocate[1]-5, userlocate[0] + 5, userlocate[1] + 5,fill="#000fff000", outline='black', width=3)


    circlecant= canvas.create_oval(cantlocate[0]-5, cantlocate[1]-5, cantlocate[0] + 5, cantlocate[1] + 5,fill="#000fff000",outline='black',width=3)


    background_image.image = background_image  # keeps a reference

    ##status bar##
    status = Label(frame,bd=1,relief=SUNKEN,anchor=W)
    status["text"] = "The distance between you and the canteen is: " + str(distance)
    status.pack(side = BOTTOM,fill="x")

if __name__ == "__main__":
    root = Tk()
    # howtogo_window(frame ,userlocate, cantlocate)
    howtogo_window(root, (472, 242), (632, 291)) 
    root.mainloop()