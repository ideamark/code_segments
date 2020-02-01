from tkinter import *
import Pmw

root = Tk()

time = Pmw.TimeCounter(root, labelpos=W, label_text='HH:MM:SS', min='00:00:00', max='23:59:59')
time.pack(padx=10, pady=5)

root.mainloop()
