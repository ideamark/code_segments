from tkinter import *

root = Tk()
root.title('Frame_Label_Button')

f = Frame(root, width=140, height=110)
xf = Frame(f, relief=GROOVE, borderwidth=2)
Label(xf, text='Hello, world!').pack(pady=10)
Button(xf, text='AAA', state=DISABLED).pack(side=LEFT, padx=5, pady=8)
Button(xf, text='BBB', command=root.quit).pack(side=RIGHT, padx=5, pady=8)
xf.place(relx=0.01, rely=0.125, anchor=NW)
Label(f, text='This is a world').place(relx=.06, rely=0.125, anchor=W)
f.pack()

root.mainloop()
