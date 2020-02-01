from tkinter import *

root = Tk()
root.title('Scrollbar_ListBox')

list = Listbox(root, height=6, width=15)

scroll = Scrollbar(root, command=list.yview)
scroll.pack(side=RIGHT, fill=Y)

list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
for item in range(30):
    list.insert(END, item)

root.mainloop()
