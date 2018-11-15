from tkinter import *

class dbllistbox(Frame):
    def __init__(self, parent=None, data_entries=[]):
        Frame.__init__(self, parent)
        self.pack()

        self.data = data_entries

        self.main_frame = Frame()
        self.main_frame.pack(fill='both', expand=True)

        self.make_listbox = Listbox(self.main_frame)
        self.make_listbox.pack(fill='both', expand=True, side=LEFT)

        # here we bind the make listbox selection to our method
        self.make_listbox.bind('<<ListboxSelect>>', self.load_models)

        self.model_listbox = Listbox(self.main_frame)
        self.model_listbox.pack(fill='both', expand=True, side=LEFT)

        # insert our items into the list box
        count = 0
        for i in self.data:
            self.make_listbox.insert(count, i[0])
            count += 1

    def load_models(self, *args):
        selection = self.make_listbox.curselection()[0]   
        # clear model listbox
        self.model_listbox.delete(0, END)

        # insert models into model listbox
        count = 0
        for data in self.data[selection][1]:
            self.model_listbox.insert(count, data)
            count += 1 

if __name__ == "__main__":
    root = Tk()
    app = dbllistbox(root, [
                ['Fruits', ['Apple', 'Banana', 'Pear']],
                ['Stationery', ['Pencil', 'Pen', 'Eraser']],
                ['Funiture', ['Chair', 'Table', 'Sofa']],
                ['Halls', ['Hall 5', 'Hall 2', 'Tamarind Hall']]])
    app.mainloop()