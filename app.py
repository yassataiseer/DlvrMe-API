import mysql.connector
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import os
#from user_manager import user
#from order_manager import order
from Users.user_template import user_template
from Orders.order_template import order_template
from models import User
app = Flask(__name__)
api = Api(app)
app.register_blueprint(user_template,url_prefix="/Users")
app.register_blueprint(order_template,url_prefix="/Orders")




@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == "__main__":
	app.run(port=5000 ,debug=True)
