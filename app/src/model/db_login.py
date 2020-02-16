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
                print("Já cadastrado")
            else:
                cursor.execute("""INSERT INTO user( name, username, password) 
                VALUES('{}','{}','{}')""".format(name, username, password))
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                conn.commit()
                conn.close()
                self.msg = "Successfully entered data!"    


    def __search__( self, req):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * FROM user WHERE username = '{}'""".format( req))
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                resul = cursor.fetchall()
                conn.close()
                return resul


    def __login__( self, req1, req2):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""SELECT * FROM user WHERE username = '{}' \
                    and password = '{}'""".format( req1, req2))
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                resul = cursor.fetchall()
                conn.close()
                return resul

    def __update__( self, username, password, name):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""UPDATE user SET name = '{}' ,username = '{}', \
                password = '{}' WHERE password = '{}'""".format( name, 
                                        username, password, password))
            conn.commit()
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                conn.close()
                self.msg = "Update successfully!"
                return self.msg
        

    def __delete_user__( self, name, password):
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""DELETE FROM user WHERE name = '{}'  \
                    and password = '{}'""".format(name, password))
            conn.commit()
        except Exception as e:
            self.error = True
            self.msg = e
        finally:
            if self.error:
                conn.close()
                return self.msg
            else:
                conn.close()
                self.msg = "Success by deleting user!"