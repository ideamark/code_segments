from tkinter import *

root = Tk()
root.title('Radiobutton_1')

var = IntVar()
for text, value in [('Passion fruit',1), ('Loganberries',2), ('Mangoes in syrup',3), ('Oranges',4), ('Apples',5), ('Grapefruit',6)]:
    Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)
var.set(3)

root.mainloop()
