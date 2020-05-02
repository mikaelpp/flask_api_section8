from flask_restful import Resource, reqparse

from models.user import UserModel


class User_register(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='no help')
    parser.add_argument('password', type=str, required=True, help='no help')

    def post(self):
        data = User_register.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'that user already exist'}

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user was succesfully registered'}, 201
