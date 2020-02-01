from tkinter import *
import Pmw

root = Tk()

st = Pmw.ScrolledText(root, borderframe=1, labelpos=N, \
            label_text='Blackmail', usehullsize=1, \
            hull_width=400, hull_height=300, \
            text_padx=10, text_pady=10, \
            text_wrap='none')
st.importfile('blackmail.txt')
st.pack(fill=BOTH, expand=1, padx=5, pady=5)

root.mainloop()
