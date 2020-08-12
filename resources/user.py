import sqlite3

from flask_restful import Resource, reqparse, request
from models.user_model import UserModel


class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Username cannot be blank.")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password cannot be blank.")

    def post(self):
        data = UserRegistration.parser.parse_args()
        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {"message": "user created successfully..."}, 201
