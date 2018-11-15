from tkinter import *
from tkinter import ttk
from sorting_functions import count_distance

def howtogo_window(userlocate, cantlocate):
    distance = count_distance(userlocate, cantlocate)
    # userlocate = (608,400)
    # cantlocate = (100, 284)
    root = Tk()
    root.wm_geometry("990x699")
    ##frame##
    bottomframe = Frame(root)
    bottomframe.pack(side =BOTTOM)

    ##button##
    button2 = ttk.Button(bottomframe, text="Back", 
                         command=quit)
    button2.pack()

    ##canvas##
    canvas = Canvas(root)
    canvas.pack(fill=BOTH, expand=1) # Stretch canvas to root window size.

    ##image + line + circle##
    background_image=PhotoImage(file="Canteen-Recommender-App/Main/NTUcampus.png")
    image = canvas.create_image(0, 0, anchor=NW, image=background_image)
    line = canvas.create_line( userlocate[0] ,userlocate[1], cantlocate[0],cantlocate[1], fill="red",width=3,arrow=LAST)


    circleuser = canvas.create_oval(userlocate[0]-5, userlocate[1]-5, userlocate[0] + 5, userlocate[1] + 5,fill="#000fff000", outline='black', width=3)


    circlecant= canvas.create_oval(cantlocate[0]-5, cantlocate[1]-5, cantlocate[0] + 5, cantlocate[1] + 5,fill="#000fff000",outline='black',width=3)


    ##status bar##
    status = Label(root,bd=1,relief=SUNKEN,anchor=W)
    status["text"] = "The distance between you and the canteen is: " + str(distance)
    status.pack(side = BOTTOM,fill="x")



    ###title and mainloop##
    root.title('Map')
    root.mainloop()

if __name__ == "__main__":
    howtogo_window((608,400), (100, 284))