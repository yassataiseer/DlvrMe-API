import mysql.connector
import os
from dotenv import load_dotenv
from decouple import config
from hashlib import sha256




class user:
    def __init__(self,username,password):
        self.username =  username
        self.password = sha256(password.encode('utf-8')).hexdigest()

    def connect():
        db =mysql.connector.connect(
        host = config('HOST') ,
        user = config('USERNAME') ,
        passwd = config('PASSWORD'),
        database = config('DATABASE'))
        return db 
    def add_user(self):
        db = user.connect()
        mycursor = db.cursor()
        boolean = user.check_if_user_exists(self)
        if boolean == True:
            return {"Status" : False}
        mycursor.execute("INSERT INTO user (Username,Password) VALUES (%s,%s)",(self.username,self.password))
        db.commit()
        mycursor.close()
        db.close()
        return {"Status" : True}
    def delete_user(self):
        db = user.connect()
        mycursor = db.cursor()
        boolean = user.check_user(self)
        if boolean == {"Status" : False}:
            return {"Status" : False}
        mycursor.execute("DELETE FROM User WHERE Username = %s ",(self.username,))
        mycursor.execute("DELETE FROM deliveries WHERE Username = %s",(self.username,))
        db.commit()
        mycursor.close()
        db.close()
        return {"Status": True}

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

#boolean = user("Eshal Taiseer","Eshal123")
#print(boolean.delete_user())

