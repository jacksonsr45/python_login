__author__ = "jacksonsr45@gmail.com"

import tkinter
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (200 // 2)
        self.root.geometry("400x200+{}+{}".format( x, y))

        self.msg = tkinter.StringVar()
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()



    def set_msg(self, msg):
        self.show_msg(msg)
        

    def show_msg(self, msg):
        self.msg.set(msg)
        if len(self.msg.get()) > 5:
            print(self.msg.get())
            messagebox.showinfo('msg', self.msg.get())


    def __labels(self, root, font, bg, text, x, y, width, height):
        label = tkinter.Label(root)
        label.configure(font=font)
        label.configure(anchor=tkinter.E)
        label.configure(bg=bg)
        label.configure(text=text)
        label.place(relx=x, rely=y, relwidth=width, relheight=height)
        return label


    def __entry(self, root, font, bg, x, y, width, height):
        entry = tkinter.Entry(root)
        entry.configure(font=font)
        entry.configure(bd=0)
        entry.configure(state=tkinter.DISABLED)
        entry.configure(bg=bg)
        entry.place(relx=x, rely=y, relwidth=width, relheight=height)
        return entry


    def __buttons(self, root, bg, font, text, state, bd, x, y, width, height, command=None):
        button = tkinter.Button(root)
        button.configure( bg=bg )
        button.configure( font=font )
        button.configure( text=text )
        button.configure(state=state)
        button.configure( bd=bd )
        button.configure( command=command )
        button.place(relx=x, rely=y, relwidth=width, relheight=height )
        return button
    

    def __frames(self, root, bg, hlbg, hlbd, x, y, width, height):
        frame = tkinter.Frame(root)
        frame.configure(bg=bg)
        frame.configure( highlightbackground=hlbg )
        frame.configure( highlightthickness=hlbd )
        frame.place( relx=x, rely=y, relwidth=width, relheight=height)
        return frame