import mysql.connector
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import os
#from user_manager import user
#from order_manager import order
from Users.user_template import user_template
from Orders.order_template import order_template
from models import User,db
from decouple import config
from flask_sqlalchemy import SQLAlchemy

host = config('HOST') 
user = config('USERNAME') 
passwd = config('PASSWORD')
database = config('DATABASE')
app = Flask(__name__)
api = Api(app)
app.register_blueprint(user_template,url_prefix="/Users")
app.register_blueprint(order_template,url_prefix="/Orders")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
db.init_app(app)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
