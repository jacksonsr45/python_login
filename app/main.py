__author__ = "jacksonsr45@gmail.com"

import tkinter
from app.src.data.app_login import Login

class Main:
    def __init__(self):
        root = tkinter.Tk()
        Login(root)
        root.mainloop()