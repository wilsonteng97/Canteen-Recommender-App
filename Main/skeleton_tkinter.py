# importing useful modules
from tkinter import *
from tkinter import ttk
import pygame
from pprint import pprint 

# Import user files
from data import *
import pygame_get_user_location as location_module
import Create_Checkbox as pref_module
import Create_DoubleListbox as listbox_module
import sorting_functions as sorting_module
import howtogo_window as howtogo_module

# Global user variables
PricePreference = [0,0,0] # [(< $5), ($5-10), (> $10)]
ItemPreference =[0,0] # [Food, Beverage]
UserPosition = (0,0) # (x-coordinate, y-coordinate)
CanteenList = [] # CanteenList sorted by distance 
CanteenList_sorted = [] # CanteenList further sorted by PricePreference & ItemPreference

# Fonts
LARGE_FONT = ("Verdana", 12)

# Functions for all Frames to use
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

# Application
class CanteenRecommender(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "NTU Canteen Recommender App")
        container = Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Preferences, Choosing, GeneralDirection):
            print(F)
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()
        frame.winfo_toplevel().geometry("990x699")
    
    def get_page(self, page_class):
        return self.frames[page_class]


# "StartPage" frame Functions
def getlocation():
    global UserPosition
    global CanteenList
    pygame.init()
    UserPosition = location_module.get_user_location()
    pygame.quit()
    CanteenList = sorting_module.sort_canteen_bydistance(Canteen, UserPosition)
    pprint(CanteenList)
    print(f"UserPosition is {UserPosition}   --> (x-coordinate, y-coordinate)")
    
# "StartPage" frame
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller        

        label = Label(self, text="NTU Canteen Recommender", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Start", 
                            command=lambda: combine_funcs(getlocation(),
                                                          controller.show_frame(Preferences)))
        button1.pack()

        button2 = ttk.Button(self, text="Quit", 
                            command=quit)
        button2.pack()
     

# "Preferences" frame Functions 
def updatePricePreference_global(chk):
    global PricePreference
    PricePreference = list(chk.state())
    print(f"PricePreference is {PricePreference} --> [(< $5), ($5-10), (> $10)]")

def updateItemPreference_global(chk):
    global ItemPreference
    ItemPreference = list(chk.state())
    print(f"ItemPreference is {ItemPreference}     --> [Food, Beverage]")

def updateCanteenList_global():
    global CanteenList
    global CanteenList_sorted
    global PricePreference
    global ItemPreference
    CanteenList_sorted = sorting_module.sortby_price_bevfood(CanteenList, 
                                                      PricePreference, 
                                                      ItemPreference)
    pprint(CanteenList_sorted)

def init_dbllistbox_choosingframe(Frame):
    global CanteenRecommender
    global Choosing
    Frame.controller.show_frame(Choosing)
    updateCanteenList_global()

# "Preferences" frame
class Preferences(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        # Leaves "Next" Button diabled if users select nothing \
        # from either "PricePreference" & "ItemPreference"
        def check_checkboxes():
            global PricePreference, ItemPreference
            if PricePreference == [0,0,0] or ItemPreference == [0,0]:
                button1.configure(state=DISABLED)
            else:
                button1.configure(state=NORMAL)   

        label = ttk.Label(self, text="We want to know your preferences!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label1 = ttk.Label(self, text="Choose your price range")
        label1.pack()
        
        chk1 = pref_module.Checkbar(self, ['< $5', '$5-10', '> $10'])
        chk1.pack()

        label2 = ttk.Label(self, text="Choose Food, Beverage, or Both!")
        label2.pack()
        
        chk2 = pref_module.Checkbar(self, ['Food', 'Beverage'])
        chk2.pack()

        button0 = ttk.Button(self, text='Update', 
                        command=lambda: combine_funcs(updatePricePreference_global(chk1), 
                                                      updateItemPreference_global(chk2),
                                                      check_checkboxes(),
                                                      print()))
        button0.pack(pady=15)
        
        button1 = ttk.Button(self, text="Next", state=DISABLED,
                                command=lambda: combine_funcs(updateCanteenList_global(),
                                                              controller.show_frame(Choosing)))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()


# "Choosing" frame
class Choosing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        label = ttk.Label(self, text="Which Canteen would you like to go to?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        def check_lstboxselected():
            lstsel = self.controller.get_page(Choosing).lst1.state()
            print(lstsel)
            if lstsel not in range(len(CanteenList)):
                button1.configure(state=DISABLED)
            else:
                button1.configure(state=NORMAL)

        button0 = ttk.Button(self, text="Select",
                                command=lambda: combine_funcs(check_lstboxselected()))
        button0.pack()

        button1 = ttk.Button(self, text="How To Go!", state=DISABLED,
                                command=lambda: combine_funcs(controller.show_frame(GeneralDirection)))
        button1.pack()

        button2 = ttk.Button(self, text="Quit", 
                            command=quit)
        button2.pack()
    
    def on_show_frame(self, event):
        global CanteenList_sorted
        print("I am being shown...")
        print(CanteenList_sorted)
        self.lst1 = listbox_module.dbllistbox(self, data_entries=CanteenList_sorted)


# "GeneralDirection" frame
class GeneralDirection(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller 
        self.bind("<<ShowFrame>>", self.on_show_frame) 
        label = ttk.Label(self, text="Thank you for using Canteen Recommender App", font=LARGE_FONT)
        label.pack()
        label = ttk.Label(self, text="Done by: Wilson Thurman Teng, Jay Yap & Wong Rui Yang")
        label.pack()
        

        button1 = ttk.Button(self, text="Quit", 
                            command=lambda: quit())
        button1.pack()
    
    def on_show_frame(self, event):
        global CanteenList
        global UserPosition     
        lstsel = self.controller.get_page(Choosing).lst1.state()
        CanteenPosition = CanteenList[lstsel]["location"]
        howtogo_module.howtogo_window(self, UserPosition, CanteenPosition)
        

# Run Application
app = CanteenRecommender()
app.mainloop()