from tkinter import *

class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)

   def state(self):
      return map((lambda var: var.get()), self.vars)

if __name__ == '__main__':
   root = Tk()
   pricerange = Checkbar(root, ['< $5', '$5-10', '> $10'])
   item = Checkbar(root, ['Food','Beverage'])
   pricerange.pack(side=TOP,  fill=X)
   item.pack(side=LEFT)
   pricerange.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(pricerange.state()), list(item.state()))

   Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()