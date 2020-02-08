from tkinter import *
from tkinter import scrolledtext


if __name__ == '__main__':
    tk = Tk()
    tk.title('Java UT Converter')
    ut_st = scrolledtext.ScrolledText(tk, height=40, exportselection=0)
    ut_st.pack(side=LEFT)
    txt_st = scrolledtext.ScrolledText(tk, height=40, exportselection=0)
    txt_st.pack(side=RIGHT)
    tk.mainloop()
