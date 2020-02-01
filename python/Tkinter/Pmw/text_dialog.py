from tkinter import *
import Pmw

root = Tk()

sketch = """Doctor: Mr. Bertenshaw?
Mr. B: Me, Doctor.
# ------Lines removed---------
Jane, you Trent, you Trillo...me doctor!"""

dialog = Pmw.TextDialog(root, scrolledtext_labelpos='n', \
                        title='Sketch', defaultbutton=0, label_text='The Hospital')
dialog.insert(END, sketch)
dialog.configure(text_state='disabled')
dialog.activate()
dialog.tkraise()

root.mainloop()
