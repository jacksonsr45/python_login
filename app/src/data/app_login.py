__author__ = "jacksonsr45@gmail.com"

import tkinter

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (200 // 2)
        self.root.geometry("400x200+{}+{}".format( x, y))