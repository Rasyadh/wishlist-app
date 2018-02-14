from flask import request
from flask_restful import Api, Resource
from main import app
from api import Wish, WishList

api = Api(app)

api.add_resource(WishList, '/api/wishlist')
api.add_resource(Wish, '/api/wishlist/<id>')