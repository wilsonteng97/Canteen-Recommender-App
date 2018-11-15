import tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self)
        self.selection = tk.Listbox(self, width=40)

        self.label.pack(side="top", fill="x", expand=False)
        self.selection.pack(side="top", fill="both", expand=True)

        self.data = {"stuff": 1, "morestuff": 2}
        self.selection.insert("end", "stuff", "morestuff")

        self.selection.bind("<<ListboxSelect>>", self.on_listbox_select)

    def on_listbox_select(self, event):
        i = self.selection.curselection()[0]
        text = self.selection.get(i)
        self.label.configure(text="new value: %s (%s)" % (self.data[text], text))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()