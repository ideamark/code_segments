from tkinter import *

root = Tk()
root.title('Message')

msg = 'Exactly. It is my belief that these sheep are laborin.'
Message(root, text=msg, bg='royalblue', fg='ivory', relief=GROOVE).pack(padx=10, pady=10)

root.mainloop()
