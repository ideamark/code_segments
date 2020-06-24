from tkinter import *


def ut_to_text(event, ut_st, txt_st):
    ...


button = Button(text='UT to Text >>')
button.bind('<Button-1>', lambda event: ut_to_text(event, ut_st, txt_st))
