import mysql.connector
import os

from decouple import config




class user:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def connect():
        db =mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "new_password",
        database = "dlvrme")
        return db 
    def add_user(self):
        db = user.connect()
        mycursor = db.cursor()
        boolean = user.check_if_user_exists(self.username)
        if boolean == True:
            return {"Status" : False}
        mycursor.execute("INSERT INTO user (Username,Password) VALUES (%s,%s)",(self.username,self.password))
        db.commit()
        mycursor.close()
        db.close()
        return {"Status" : True}


    def check_user(self):
        db = user.connect()
        mycursor = db.cursor()
        mycursor.execute("SELECT Username FROM user WHERE Username = (%s) AND Password = (%s) ",(self.username,self.password))
        data = mycursor.fetchall()
        mycursor.close()
        db.close()
        if len(data)==0:
            return {"Status" : False}
        else:
            return {"Status" : True}

        
    def check_if_user_exists(self):
        db = user.connect()
        mycursor = db.cursor()
        mycursor.execute("SELECT Username FROM user WHERE Username = (%s) ",(self.username,))
        data = mycursor.fetchall()
        mycursor.close()
        db.close()
        if len(data)==0:
            return  False
        else:
            return  True

boolean = user("Yassa Taiseer","yassa123")
print(boolean.check_user())

