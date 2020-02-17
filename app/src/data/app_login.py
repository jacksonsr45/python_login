__author__ = "jacksonsr45@gmail.com"

import tkinter
from tkinter import messagebox
from app.src.model.db_login import User
from app.src.data.new_user import New_User


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

        self.__label(self.frame, ("Ubunto", 14), "white", "Username:", 0, 0.2, 0.3, 0.15)

        self.user_name = self.__entry(self.frame, ("Ubunto", 14), self.username, "normal", "white", 
                        0.3, 0.2, 0.6, 0.15)
        self.user_name.focus()

        self.__label(self.frame, ("Ubunto", 14), "white", "Password:", 0, 0.5, 0.3, 0.15)

        self.__entry(self.frame, ("Ubunto", 14), self.password, "normal", "white", 
                        0.3, 0.5, 0.6, 0.15, "*")

        self.__button(self.root, "white", ("Ubunto", 8), "CREATE OR UPDATE USER", "normal", 0, 
                        0.1, 0.7, 0.35, 0.15, command= self.__new_user)
        
        self.__button(self.root, "white", ("Ubunto", 14), "LOGIN", "normal", 0, 
                        0.5, 0.7, 0.35, 0.15, command= self.__login)


    def set_msg(self, msg):
        self.show_msg(msg)
        

    def show_msg(self, msg):
        self.msg.set(msg)
        if len(self.msg.get()) > 5:
            print(self.msg.get())
            messagebox.showinfo('msg', self.msg.get())

    
    def __login(self):
        result = User().__login__( self.username.get(), self.password.get())
        if result:
            self.msg.set("Successfully Login")
            messagebox.showinfo('msg', self.msg.get())
        else:
            self.msg.set("Incorrect User or Password")
            messagebox.showinfo('msg', self.msg.get())


    def __new_user(self):
        self.root.destroy()
        new_user = tkinter.Tk()
        New_User(new_user)
        new_user.mainloop()


    def __label(self, root, font, bg, text, x, y, width, height):
        label = tkinter.Label(root)
        label.configure(font=font)
        label.configure(anchor=tkinter.E)
        label.configure(bg=bg)
        label.configure(text=text)
        label.place(relx=x, rely=y, relwidth=width, relheight=height)
        return label


    def __entry(self, root, font, textvariable, state, bg, x, y, width, height, show=None):
        entry = tkinter.Entry(root)
        entry.configure(font=font)
        entry.configure(textvariable=textvariable)
        entry.configure(bd=0)
        entry.configure(state=state)
        entry.configure(bg=bg)
        entry.configure(show=show)
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