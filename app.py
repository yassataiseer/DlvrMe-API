import mysql.connector
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import os
from user_manager import user
app = Flask(__name__)
api = Api(app)

"""Users"""
class mk_user(Resource):
    def get(self,Username,Password):
        status = user.add_user(Username,Password)
        return status

api.add_resource(mk_user,"/mk_user/<string:Username>/<string:Password>")

if __name__ == "__main__":
	app.run(debug=True)
