from flask_restful import Resource, reqparse
from project.accounts.models import UserModel

class RegisterUser(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('firstname',
        type=str,
        required = True,
        help='This field cannot be left blank'
    )

    parser.add_argument('lastname',
        type=str,
        required = True,
        help='This field cannot be left blank'
    )

    parser.add_argument('email',
        type=str,
        required = True,
        help='This field cannot be left blank'
    )

    parser.add_argument('username',
        type=str,
        required = True,
        help='This field cannot be left blank'
    )

    parser.add_argument('password',
        type=str,
        required = True,
        help='This field cannot be left blank'
    )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        # check if user already exists
        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username {} already exists'.format(data['username'])}, 400
        
        # create new user object
        user = UserModel(**data)

        # save user to database
        user.save_user_to_db()
        return {'message':'User was successfully created'}, 201
