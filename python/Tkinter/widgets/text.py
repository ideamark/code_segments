from tkinter import *

root = Tk()
root.title('Text')

text = Text(root, height=26, width=50)
scroll = Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scroll.set)

text.tag_configure('bold_italics', font=('Verdana', 12, 'bold', 'italic'))
text.tag_configure('big', font=('Verdana', 24, 'bold'))
text.tag_configure('color', foreground='blue', font=('Tempus Sans ITC', 14))
text.tag_configure('groove', relief=GROOVE, borderwidth=2)

text.tag_bind('bite','<1>', lambda e,t=text: t.insert(END, 'Hello, world!'))

text.insert(END, 'aaaaaaaaaaaa\n')
text.insert(END, 'bbbbbbbbbbb\n', 'bold_italics')
text.insert(END, 'cccccc\n', 'big')
text.insert(END, 'ddddddddd\n', 'color')
text.insert(END, 'eeeeeeeee\n', 'groove')

button = Button(text, text='How are you?')
text.window_create(END, window=button)
photo = PhotoImage(file='image.png')
text.image_create(END, image=photo)

text.insert(END, '\nI dare you to click on this\n', 'bite')
text.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
