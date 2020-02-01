from tkinter import *
from tkinter.messagebox import *
import Pmw

class App:
    def __init__(self, master):
        self.result = Pmw.EntryField(master, entry_width=8, value='', \
                                     label_text='Returned value:  ', labelpos=W, labelmargin=1)
        self.result.pack(padx=15, pady=15)

root = Tk()
question = App(root)

button = askquestion('Question:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = showinfo('Information:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = showwarning('Warning:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = showerror('Error:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = askokcancel('OK or Cancel:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = askyesno('Yes or No:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')
#button = askretrycancel('Retry or Cancel:', 'Oh Dear, did somebody\nsay mattress to Mr lambert?')

question.result.setentry(button)
root.mainloop()
