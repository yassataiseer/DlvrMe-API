from flask import Flask, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Users.user_manager import user
user_template = Blueprint("user_template",__name__)

api = Api(user_template)

"""Users"""
class mk_user(Resource):
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.add_user()
        return jsonify(status)

class validate_user(Resource):
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.check_user()
        return jsonify(status)

class delete_user(Resource):
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.delete_user()
        return jsonify(status)



api.add_resource(mk_user,"/mk_user/<string:Username>/<string:Password>")
api.add_resource(validate_user,"/validate_user/<string:Username>/<string:Password>")
api.add_resource(delete_user,"/delete_user/<string:Username>/<string:Password>")



