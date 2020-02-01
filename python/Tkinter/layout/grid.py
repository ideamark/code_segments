from tkinter import *

root = Tk()

class App:
    def __init__(self, master):
        Label(master, text='Old Password:').grid(row=0, column=1, sticky=W)
        Label(master, text='New Password:').grid(row=1, column=2, sticky=W)
        Label(master, text='Enter New Password Again:').grid(row=2, column=3, sticky=W)

display = App(root)
root.mainloop()
