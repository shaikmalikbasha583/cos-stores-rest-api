import os
from datetime import timedelta

from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required
from flask_restful import Api, Resource, reqparse

from resources.item import Item, ItemList
from resources.user import UserRegistration
from security import authenticate, identity
from resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = "secret-key"
api = Api(app)

# configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authenticate, identity)


@jwt.auth_response_handler
def custom_response_handler(access_token, identity):
    return jsonify({
        "access_token": access_token.decode('utf-8'),
        "user_id": identity.id
    })


api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegistration, "/register")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, host='127.0.0.1', debug=True)
