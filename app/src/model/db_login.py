__author__ = "jacksonsr45@gmail.com"

import sqlite3

class User:
    def __init__(self):
        self.error = False
        self.msg = " "


    def __create__(self):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute('CREATE TABLE IF NOT EXISTS user ( id integer  \
                PRIMARY KEY AUTOINCREMENT NULL, name text, username text, \
                    password text)')
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                conn.close()
            

    def __save__( self, name, username, password):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * FROM user WHERE name = '{}' \
                        and username = '{}'""".format( name, username))
            if (cursor.fetchall()):
                self.msg = "User already registered!!"
                return self.msg  
            else:
                cursor.execute("""INSERT INTO user( name, username, password) 
                VALUES('{}','{}','{}')""".format(name, username, password))
                conn.commit()
                conn.close()
                self.msg = "Successful user!"
                return self.msg  
        except Exception as e:
            self.error = True
            self.msg = e
        conn.close()
                  

    def __login__( self, req1, req2):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * FROM user WHERE username = '{}' \
                    and password = '{}'""".format( req1, req2))
            self.value = cursor.fetchall()
            conn.close()
            return self.value 
        except Exception as e:
            self.error = True
            self.msg = e
        conn.close() 

    def __update__( self, username, password, name):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * FROM user WHERE name = '{}'""".format(name))
            if cursor.fetchall():
                cursor.execute("""UPDATE user SET username = '{}', \
                    password = '{}' WHERE name = '{}'""".format( username, password,
                                        name))
                conn.commit()
                self.msg = "Successful update user!"
                return self.msg
            else: 
                self.msg = "ERROR!!"
                return self.msg
            
        except Exception as e:
            self.error = True
            self.msg = e
            return self.msg
        
        conn.close()