import mysql.connector
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import os
from Users.user_template import user_template
from Orders.order_template import order_template
##imports of packages made for users and deliveries tables
from models import User,db
from decouple import config
from flask_sqlalchemy import SQLAlchemy

host = config('HOST') 
user = config('USERNAME') 
passwd = config('PASSWORD')
database = config('DATABASE')
#load env var
app = Flask(__name__)
api = Api(app)
app.register_blueprint(user_template,url_prefix="/Users")
app.register_blueprint(order_template,url_prefix="/Orders")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+passwd+'@'+host+'/'+database
##connect to mysql via SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
#app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_recycle': 299,
    'pool_timeout': 20,
    'pool_size': 10,
    'max_overflow': 5,
}
db.init_app(app)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
## return 404 for when app is run on base link('/')

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)
