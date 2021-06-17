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
        #convert to sha256 for user's privacy

    def connect():
        ##debugging function
        db =mysql.connector.connect(
        host = config('HOST') ,
        user = config('USERNAME') ,
        passwd = config('PASSWORD'),
        database = config('DATABASE'))
        return db 
    def add_user(self):
        if not user.check_if_user_exists(self):
            query = User(Username=self.username,Password=self.password)
            db.session.add(query)
            db.session.commit()
            #add user to db
            return {"Status" : True}
        return {"Status" : False}

    def delete_user(self):
        User.query.filter_by(Username=self.username).delete()
        db.session.commit()
        #delete user from db
        return {"Status": True}

    def check_user(self):
        exists = bool(db.session.query(User).filter_by(Username=self.username,Password=self.password).first())
        #check to see if user exists inside of database
        #meant to validate user
        return {"Status" : exists}
        
    def check_if_user_exists(self):
        exists = bool(db.session.query(User).filter_by(Username=self.username).first())
        #check to see if the Username is already taken.
        return exists

#boolean = user("Yassa Taiseer","yassa123")
#print(boolean.check_user())
#print(boolean.delete_user())
