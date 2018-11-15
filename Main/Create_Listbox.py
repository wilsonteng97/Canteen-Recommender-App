from tkinter import *

def print_selections():
    clicked_items = l.curselection()
    print(clicked_items)
    for item in clicked_items:
        print(l.get(item))


def delete_entry():
    clicked_items = l.curselection()
    for item in clicked_items:
        print(l.delete(item))

if __name__ == '__main__':
    root = Tk()
    l = Listbox(root, width=30, height=15, selectmode=MULTIPLE)
    l.insert(1, "C++")
    l.insert(2, "C#")
    l.insert(3, "Python")
    l.insert(4, "Java")
    l.insert(5, "Javascript")
    l.pack()

    def lalala():
        selection = l.curselection()
        print(selection[0])

    button = Button(root, text="print", command=lalala)
    button.pack()
    lst = ["one", "two", "three"]


    button_delete = Button(root, text="delete", command=delete_entry).pack()
    root.geometry("400x400+120+120")
    root.mainloop()