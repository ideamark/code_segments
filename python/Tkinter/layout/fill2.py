from tkinter import *

root = Tk()

class App:
    def __init__(self, master):
        Button(master, text='Left').pack(side=LEFT, fill=BOTH, expand=YES)
        Button(master, text='Center').pack(side=LEFT, fill=BOTH, expand=YES)
        Button(master, text='Right').pack(side=LEFT, fill=BOTH, expand=YES)
        master.geometry('300x200')

display = App(root)
root.mainloop()
