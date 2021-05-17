from typing import ItemsView
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import  pymysql
from decouple import config

host = config('HOST') 
user = config('USERNAME') 
passwd = config('PASSWORD')
database = config('DATABASE')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class User(db.Model):
    Username = db.Column(db.String(255), unique=True, nullable=False, primary_key=True)
    Password = db.Column(db.String(255),  nullable=False)

class deliveries(db.Model):
    Username = db.Column(db.String(255), nullable=False, primary_key=True)
    Address = db.Column(db.String(255), unique=True, nullable=False)
    Latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)
    Item = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.Float(), nullable=False)
    User_Info = db.Column(db.String(255), nullable=False)

