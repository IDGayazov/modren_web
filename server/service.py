from flask_restful import Resource, reqparse
from flask import jsonify, request
from main import db
from orm import UserModel

parser = reqparse.RequestParser()
parser.add_argument('username', required=True)
parser.add_argument('password', required=True)
parser.add_argument('role', required=False)
parser.add_argument('firstname', required=False)
parser.add_argument('lastname', required=False)


class AllUsers(Resource):

    def get(self):
        return UserModel.query().all()

class UserRegustration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return { 'message': 'User {} already created'.format(data['username'])}

        new_user = UserModel(
            username = data['username'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            password = UserModel.generate_hash(data['passsword']),
            role = data['role']
        )

        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except Exception as e:
            return {
                'message': str(e)
                }, 500

    