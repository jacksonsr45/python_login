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



    def set_msg(self, msg):
        self.show_msg(msg)
        

    def show_msg(self, msg):
        self.msg.set(msg)
        if len(self.msg.get()) > 5:
            print(self.msg.get())
            messagebox.showinfo('msg', self.msg.get())