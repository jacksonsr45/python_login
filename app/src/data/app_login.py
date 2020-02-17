__author__ = "jacksonsr45@gmail.com"

import tkinter
from tkinter import messagebox
from app.src.model.db_login import User


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (200 // 2)
        self.root.geometry("400x200+{}+{}".format( x, y))
        self.root.resizable(width=False, height=False)

        self.msg = tkinter.StringVar()
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.frame = self.__frame(self.root, "white", "black", 1, 0.05, 0.05, 0.9, 0.9)

        self.__label(self.frame, ("Ubunto", 14), "white", "Name:", 0, 0.2, 0.3, 0.15)

        self. name = self.__entry(self.frame, self.username, ("Ubunto", 14), "normal", 
                                "white", 0.3, 0.2, 0.6, 0.15)
        self.name.focus()

        self.__label(self.frame, ("Ubunto", 14), "white", "Password:", 0, 0.5, 0.3, 0.15)

        self.__entry(self.frame, ("Ubunto", 14), self.password, "normal", "white", 
                        0.3, 0.5, 0.6, 0.15)

        self.__button(self.root, "white", ("Ubunto", 14), "CREATE USER", "normal", 0, 
                        0.1, 0.7, 0.35, 0.15, lambda new_user = self.__new_user: new_user())
        
        self.__button(self.root, "white", ("Ubunto", 14), "LOGIN", "normal", 0, 
                        0.5, 0.7, 0.35, 0.15, lambda login = self.__login, 
                        n= self.name.get(), p= self.password.get(): login( n, p))


    def set_msg(self, msg):
        self.show_msg(msg)
        

    def show_msg(self, msg):
        self.msg.set(msg)
        if len(self.msg.get()) > 5:
            print(self.msg.get())
            messagebox.showinfo('msg', self.msg.get())

    
    def __login(self, n, p):
        result = User().__login__( n, p)
        if result:
            self.msg.set("Successfully Login")
            messagebox.showinfo('msg', self.msg.get())
        else:
            self.msg.set("Incorrect User or Password")
            messagebox.showinfo('msg', self.msg.get())


    def __new_user(self):
        pass


    def __label(self, root, font, bg, text, x, y, width, height):
        label = tkinter.Label(root)
        label.configure(font=font)
        label.configure(anchor=tkinter.E)
        label.configure(bg=bg)
        label.configure(text=text)
        label.place(relx=x, rely=y, relwidth=width, relheight=height)
        return label


    def __entry(self, root, font, textvariable, state, bg, x, y, width, height):
        entry = tkinter.Entry(root)
        entry.configure(font=font)
        entry.configure(textvariable=textvariable)
        entry.configure(bd=0)
        entry.configure(state=state)
        entry.configure(bg=bg)
        entry.place(relx=x, rely=y, relwidth=width, relheight=height)
        return entry


    def __button(self, root, bg, font, text, state, bd, x, y, width, height, command=None):
        button = tkinter.Button(root)
        button.configure( bg=bg )
        button.configure( font=font )
        button.configure( text=text )
        button.configure(state=state)
        button.configure( bd=bd )
        button.configure( command=command )
        button.place(relx=x, rely=y, relwidth=width, relheight=height )
        return button
    

    def __frame(self, root, bg, hlbg, hlbd, x, y, width, height):
        frame = tkinter.Frame(root)
        frame.configure(bg=bg)
        frame.configure( highlightbackground=hlbg )
        frame.configure( highlightthickness=hlbd )
        frame.place( relx=x, rely=y, relwidth=width, relheight=height)
        return frame