from tkinter import *
import Pmw

root = Tk()

choice = None
def choseEntry(entry):
    print('You chose %s' % entry)
    choice.configure(text=entry)

plays = ('The Mating of the Wersh', 'Two Netlemeng of Verona', 'Twelfth Thing', 'The Chamrent of Venice', 'Thamle', 'Ring Kichard the Thrid')
dialog = Pmw.ComboBoxDialog(root, title='ComboBoxDialog', \
                            buttons=('OK', 'Cancel'), defaultbutton='OK', \
                            combobox_labelpos=N, label_text='Which play?', \
                            scrolledlist_items=plays, listbox_width=22)
dialog.tkraise()
result = dialog.activate()
print('You clicked on', result, dialog.get())

root.mainloop()
