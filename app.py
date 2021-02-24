import mysql.connector
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import os
from user_manager import user
from order_manager import order
app = Flask(__name__)
api = Api(app)

"""Users"""
class mk_user(Resource):
    def get(self,Username,Password):
        status = user.add_user(Username,Password)
        return status

class validate_user(Resource):
    def get(self,Username,Password):
        status = user.check_user(Username,Password)
        return status
"""Orders"""
class mk_order(Resource):
    def get(self,Username,Address,Item,Price,User_Info):
        status = order.add_order(Username,Address,Item,Price,User_Info)
        return status

api.add_resource(mk_user,"/mk_user/<string:Username>/<string:Password>")
api.add_resource(validate_user,"/validate_user/<string:Username>/<string:Password>")
api.add_resource(mk_order,"/mk_order/<string:Username>/<string:Address>/<string:Item>/<float:Price>/<string:User_Info>")


if __name__ == "__main__":
	app.run( host="10.0.0.53", port=5000 ,debug=True)
