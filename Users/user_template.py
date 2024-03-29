from flask import Flask, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Users.user_manager import user
from flask_httpauth import HTTPBasicAuth
user_template = Blueprint("user_template",__name__)## extends app.py

api = Api(user_template)
auth = HTTPBasicAuth()##instance of basic auth


USER_DATA = {
    "Yassa Taiseer": "yassa123"
}## Username&Password for basic auth
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
## Basic Auth Setup

"""Users"""
## when user() is used
## user_manager.py is called
class mk_user(Resource):
    @auth.login_required
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.add_user()
        return jsonify(status)
class validate_user(Resource):
    @auth.login_required
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.check_user()
        return jsonify(status)
class delete_user(Resource):
    @auth.login_required
    def get(self,Username,Password):
        boolean = user(Username,Password)
        status = boolean.delete_user()
        return jsonify(status)

## Api routes
api.add_resource(mk_user,"/mk_user/<string:Username>/<string:Password>")
api.add_resource(validate_user,"/validate_user/<string:Username>/<string:Password>")
api.add_resource(delete_user,"/delete_user/<string:Username>/<string:Password>")



