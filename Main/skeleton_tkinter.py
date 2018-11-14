from tkinter import *
from tkinter import ttk
import pygame

import pygame_get_user_location as location_module

LARGE_FONT = ("Verdana", 12)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


class CanteenRecommender(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "NTU Canteen Recommender App")
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PricePreference, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="NTU Canteen Recommender", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Start", 
                            command=lambda: controller.show_frame(PricePreference))
        button1.pack()

        button2 = ttk.Button(self, text="Quit", 
                            command=quit)
        button2.pack()
     
     
def getlocation():
    pygame.init()
    location_module.get_user_location()
    pygame.quit()

class PricePreference(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = ttk.Label(self, text="Choose your price range")
        label.pack()
        
        chk = ttk.Checkbutton(self, text="< $5")
        chk.pack()
        chk = ttk.Checkbutton(self, text="$5-10")
        chk.pack()
        chk = ttk.Checkbutton(self, text="> $10")
        chk.pack()

        button1 = ttk.Button(self, text="Next", 
                            command=lambda: combine_funcs(getlocation(), controller.show_frame(PageTwo)))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="PageTwo", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = ttk.Button(self, text="PageOne", 
        #                     command=lambda: controller.show_frame(PageOne))
        # button2.pack()


app = CanteenRecommender()
app.mainloop()
