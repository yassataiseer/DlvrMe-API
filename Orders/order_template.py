from flask import Flask, jsonify,Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from Orders.order_manager import order
order_template = Blueprint("order_template",__name__)

api = Api(order_template)

"""Orders"""
class mk_order(Resource):
    def get(self,Username,Address,Item,Price,User_Info):
        status = order.add_order(Username,Address,Item,Price,User_Info)
        return jsonify(status)
class del_order(Resource):
    def get(self,Username,Address,Item,Price,User_Info):
        status = order.delete_order(Username,Address,Item,Price,User_Info)
        return jsonify(status)
class all_order(Resource):
    def get(self):
        data = order.get_order()
        return jsonify(data)
class spec_order(Resource):
    def get(self,Username):
        data = order.get_order_specific_person(Username)
        return jsonify(data)
class find_address(Resource):
    def get(self,Address):
        status = order.grab_address(Address)
        return jsonify(status)
class validate_address(Resource):
    def get(self,Address):
        status = order.validate_address(Address)
        return jsonify(status)

api.add_resource(mk_order,"/mk_order/<string:Username>/<string:Address>/<string:Item>/<float:Price>/<string:User_Info>")
api.add_resource(del_order,"/del_order/<string:Username>/<string:Address>/<string:Item>/<float:Price>/<string:User_Info>")
api.add_resource(all_order,"/all_order")
api.add_resource(spec_order,"/spec_order/<string:Username>")
api.add_resource(find_address,"/find_address/<string:Address>")
api.add_resource(validate_address,"/validate_address/<string:Address>")

