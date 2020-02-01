from tkinter import *

# How to use: Press Tab or Disable button.

class Navigation:
    def __init__(self, master):
        frame = Frame(master, takefocus=1, highlightthickness=2, highlightcolor='blue')
        Label(frame, text='    ').grid(row=0, column=0, sticky=W)
        Label(frame, text='    ').grid(row=0, column=5, sticky=W)
        self.B1 = self.mkbutton(frame, 'B1', 1)
        self.B2 = self.mkbutton(frame, 'B2', 2)
        self.B3 = self.mkbutton(frame, 'B3', 3)
        self.B4 = self.mkbutton(frame, 'B4', 4)

        frame2 = Frame(master, takefocus=1, highlightthickness=2, highlightcolor='green')
        Label(frame2, text='    ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='    ').grid(row=0, column=4, sticky=W)
        self.Disable = self.mkbutton(frame2, 'Disable', 1, self.disable)
        self.Enable = self.mkbutton(frame2, 'Enable', 2, self.enable)
        self.Focus = self.mkbutton(frame2, 'Focus', 3, self.focus)

        frame3 = Frame(master, takefocus=1, highlightthickness=2, highlightcolor='yellow')
        Label(frame3, text='    ').grid(row=0, column=0, sticky=W)
        Label(frame2, text='    ').grid(row=0, column=4, sticky=W)
        self.text = Text(frame3, width=20, height=3, highlightthickness=2)
        self.text.insert(END, 'Tabs are valid here')
        self.text.grid(row=0, column=1, columnspan=3)

        frame.pack(fill=X, expand=1)
        frame2.pack(fill=X, expand=1)
        frame3.pack(fill=X, expand=1)

    def mkbutton(self, frame, button, col, action=None):
        button = Button(frame, text=button, highlightthickness=2)
        button.grid(padx=10, pady=6, row=0, column=col, sticky=NSEW)
        if action:
            button.config(command=action)
        return button

    def disable(self):
        self.B2.configure(state=DISABLED, background='cadetblue')
        self.Focus.configure(state=DISABLED, background='cadetblue')

    def enable(self):
        self.B2.configure(state=NORMAL, background=self.B1.cget('background'))
        self.Focus.configure(state=NORMAL, background=self.B1.cget('background'))

    def focus(self):
        self.B3.focus_set()

root = Tk()
root.title('Navigation')
top = Navigation(root)
quit = Button(root, text='Quit', command=root.destroy)
quit.pack(side=BOTTOM, pady=5)

root.mainloop()
