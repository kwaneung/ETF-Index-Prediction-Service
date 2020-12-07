# import pymysql
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import userDAO
import service

app = Flask(__name__)
api = Api(app)


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        rows = userDAO.getUser()  # id, name

        if (id, passwd) in rows:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}


class Getuser(Resource):
    def get(self):
        # 튜플을 딕셔너리로 변환
        return {i[0]: i[1] for i in userDAO.getUser()}


class Insertuser(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        return userDAO.insertUser(id, passwd)


class Deleteuser(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        args = parser.parse_args()

        id = args['ID']
        userDAO.deleteUser(id)
        return "delete"


class Updateuser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        tmp = userDAO.getUser()
        print(tmp)
        tmp = [i[0] for i in tmp]
        if id in tmp:
            userDAO.updateUser(id, passwd)
            return "success"
        else:
            return "fail"


api.add_resource(Login, '/login')
api.add_resource(Getuser, '/getuser')
api.add_resource(Insertuser, '/insertuser')
api.add_resource(Deleteuser, '/deleteuser')
api.add_resource(Updateuser, '/updateuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
