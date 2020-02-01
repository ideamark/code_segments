from tkinter import *

root = Tk()

class App:
    def __init__(self, master):
        Button(master, text='Left').place(relx=0.15, rely=0.20, anchor=S)
        Button(master, text='Center').place(relx=0.5, rely=0.48, anchor=CENTER)
        Button(master, text='Right').place(relx=0.99, rely=0.99, anchor=SE)

display = App(root)
root.mainloop()
