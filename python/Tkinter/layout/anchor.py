from tkinter import *

root = Tk()

class App:
    def __init__(self, master):
        Button(master, text='Left').pack(anchor=NW)
        Button(master, text='Center').pack(anchor=CENTER)
        Button(master, text='Right').pack(anchor=SE)
        master.geometry('300x100')

display = App(root)
root.mainloop()
