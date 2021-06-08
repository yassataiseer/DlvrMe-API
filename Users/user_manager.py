import mysql.connector
import os
from dotenv import load_dotenv
from decouple import config
from hashlib import sha256
from flask_sqlalchemy import SQLAlchemy
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from models import User,db
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
        try:
            query = User(Username=self.username,Password=self.password)
            db.session.add(query)
            db.session.commit()
            return {"Status" : True}
        except:
            return {"Status" : False}
    def delete_user(self):
        try:
            User.query.filter_by(Username=self.username).delete()
            db.session.commit()
            return {"Status": True}
        except:
            return {"Status":False}
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
        exists = bool(db.session.query(User).filter_by(Username=self.username).first())
        return exists

boolean = user("Yassa Taiseer","yassa123")
print(boolean.add_user())
#print(boolean.delete_user())
