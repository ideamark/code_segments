from tkinter import *

root = Tk()

class App:
    def __init__(self, master):
        Button(master, text='Left').pack(side=LEFT, fill=X, expand=YES)
        Button(master, text='Center').pack(side=LEFT, fill=X, expand=YES)
        Button(master, text='Right').pack(side=LEFT, fill=X, expand=YES)
        master.geometry('500x50')

display = App(root)
root.mainloop()
