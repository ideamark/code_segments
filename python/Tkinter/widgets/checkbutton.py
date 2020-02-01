from tkinter import *

root = Tk()
root.title('Checkbutton')

class Dummy: pass
var = Dummy()
for castmember, row, column, status in [ \
    ('John Cleese',0,0,NORMAL), \
    ('Eric Idle',0,1,NORMAL), \
    ('Graham Chapman',1,0,DISABLED), \
    ('Terry Jones',1,1,NORMAL), \
    ('Michael Palin',2,0,NORMAL), \
    ('Terry Gilliam',2,1,NORMAL)]:
    setattr(var, castmember, IntVar())
    Checkbutton(root, text=castmember, state=status, anchor=W, variable=getattr(var,castmember)).grid(row=row, column=column, sticky=W)

root.mainloop()
