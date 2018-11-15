from tkinter import *
from tkinter import ttk
import pygame
from pprint import pprint 

from data import *
import pygame_get_user_location as location_module
import Create_Checkbox as pref_module
import sorting_functions as sorting_module

# Global user variables
PricePreference = [0,0,0] # [(< $5), ($5-10), (> $10)]
ItemPreference =[0,0] # [Food, Beverage]
UserPosition = (0,0) # (x-coordinate, y-coordinate)
CanteenList = []
SelectedCanteen = []

LARGE_FONT = ("Verdana", 12)

# Functions for all Frames to use
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

        for F in (StartPage, Preferences, Choosing, GeneralDirection):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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
    global PricePreference
    global ItemPreference
    CanteenList = sorting_module.sortby_price_bevfood(CanteenList, 
                                                      PricePreference, 
                                                      ItemPreference)
    pprint(CanteenList)
        
# "Preferences" frame
class Preferences(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
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
                                                      updateCanteenList_global(),
                                                      print()))
        button0.pack(pady=15)
        
        button1 = ttk.Button(self, text="Next", state=DISABLED,
                                command=lambda: controller.show_frame(Choosing))
        button1.pack()

        button2 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()

class Choosing(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tell me how to go!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        global CanteenList
        global SelectedCanteen

        def updatelistbox(lst):
            for cant in Canteen:
                # print(cant, "\n")
                lst.insert(END, cant["name"])

        def refresh_itemprice(lst):
            # lst.delete(0,'end')
            selection = lst.curselection()
            print(selection[0])
            for foodcourt in sorting_module.return_selected_foodcourt(CanteenList, selection_tuple=selection[0]):
                print(foodcourt)
                for items in foodcourt[1]:
                    item_entry = str(items[0]) + ": $" + str(1)
                    lst.insert(item_entry)       
        
        lst1 = Listbox(self, width=30, height=15, selectmode=SINGLE)
        updatelistbox(lst1)
        lst1.pack(side=LEFT)
        
        lst2 = Listbox(self, width=30, height=15)
        lst2.pack(side=LEFT)

        button0 = ttk.Button(self, text="Select", 
                            command=lambda: print(lst2.curselection()))
        button0.pack(pady=10)

        button1 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

# "GeneralDirection" frame
class GeneralDirection(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = ttk.Label(self, text="Directions", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


app = CanteenRecommender()
app.mainloop()