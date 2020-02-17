__author__ = "jacksonsr45@gmail.com"

import tkinter
from tkinter import messagebox
from app.src.model.db_login import User


class New_User:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (200 // 2)
        self.root.geometry("400x200+{}+{}".format( x, y))
        self.root.resizable(width=False, height=False)

        self.msg = tkinter.StringVar()
        self.name_user = tkinter.StringVar()
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.frame = self.__frame(self.root, "white", "black", 1, 0.05, 0.05, 0.9, 0.9)

        self.__label(self.frame, ("Ubunto", 14), "white", "Name:", 0, 0, 0.3, 0.15)

        self.name = self.__entry(self.frame, ("Ubunto", 14), self.name_user, "normal", "white", 
                        0.3, 0, 0.6, 0.15)
        self.name.focus()

        self.__label(self.frame, ("Ubunto", 14), "white", "Username:", 0, 0.2, 0.3, 0.15)

        self.__entry(self.frame, ("Ubunto", 14), self.username, "normal", "white", 
                        0.3, 0.2, 0.6, 0.15)

        self.__label(self.frame, ("Ubunto", 14), "white", "Password:", 0, 0.5, 0.3, 0.15)

        self.__entry(self.frame, ("Ubunto", 14), self.password, "normal", "white", 
                        0.3, 0.5, 0.6, 0.15, "*")

        self.__button(self.root, "white", ("Ubunto", 14), "UPDATE USER", "normal", 0, 
                        0.1, 0.7, 0.35, 0.15, command= self.__update_user)
        
        self.__button(self.root, "white", ("Ubunto", 14), "SAVE", "normal", 0, 
                        0.5, 0.7, 0.35, 0.15, command= self.__save)

    
    def __save(self):
        if User().__save__( self.name_user.get(), self.username.get(), 
                            self.password.get()):
            self.msg.set("Successful user!")
            self.root.destroy()
            from app.src.data.app_login import Login
            root = tkinter.Tk()
            Login(root).set_msg(self.msg.get())
            root.mainloop()
        else:
            self.msg.set("ERROR creating user")
            messagebox.showinfo('msg', self.msg.get())


    def __update_user(self):
        pass


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