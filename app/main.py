__author__ = "jacksonsr45@gmail.com"

import tkinter
from .import *

class Main:
    def __init__(self):
        root = tkinter.Tk()
        msg = User().__create__()
        Login( root).set_msg(msg)
        root.mainloop()