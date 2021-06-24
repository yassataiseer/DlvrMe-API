from flask import Flask, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Orders.order_manager import order##import order package
from flask_httpauth import HTTPBasicAuth



order_template = Blueprint("order_template",__name__)## extends app.py

api = Api(order_template)
auth = HTTPBasicAuth()

USER_DATA = {
    "Yassa Taiseer": "yassa123"
}
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
# Setup of basic auth

"""Orders"""
## when order.function() the order_manager.py is called
class mk_order(Resource):
    @auth.login_required
    def get(self,Username,Address,Item,Price,User_Info):
        status = order.add_order(Username,Address,Item,Price,User_Info)
        return jsonify(status)
class del_order(Resource):
    @auth.login_required
    def get(self,Username,Address,Item,Price,User_Info):
        status = order.delete_order(Username,Address,Item,Price,User_Info)
        return jsonify(status)
class all_order(Resource):
    @auth.login_required
    def get(self):
        data = order.get_order()
        return jsonify(data)
class spec_order(Resource):
    @auth.login_required
    def get(self,Username):
        data = order.get_order_specific_person(Username)
        return jsonify(data)
class find_address(Resource):
    @auth.login_required
    def get(self,Address):
        status = order.grab_address(Address)
        return jsonify(status)
class validate_address(Resource):
    @auth.login_required
    def get(self,Address):
        status = order.validate_address(Address)
        return jsonify(status)

## api routes
api.add_resource(mk_order,"/mk_order/<string:Username>/<string:Address>/<string:Item>/<float:Price>/<string:User_Info>")
api.add_resource(del_order,"/del_order/<string:Username>/<string:Address>/<string:Item>/<float:Price>/<string:User_Info>")
api.add_resource(all_order,"/all_order")
api.add_resource(spec_order,"/spec_order/<string:Username>")
api.add_resource(find_address,"/find_address/<string:Address>")
api.add_resource(validate_address,"/validate_address/<string:Address>")

