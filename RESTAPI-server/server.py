# import pymysql
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

import serverDAO
import service

app = Flask(__name__)
api = Api(app)


# connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
#                           db='ETFIPS', charset='utf8')
# cur = connect.cursor()

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        rows = serverDAO.getUser()  # id, name

        # print('Request ID : ' + ID)
        # print('Request passwd : ' + passwd)

        if (id, passwd) in rows:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}


class Getuser(Resource):
    def get(self):
        # 튜플을 딕셔너리로 변환
        return {i[0]: i[1] for i in serverDAO.getUser()}


class Insertuser(Resource):
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        id = args['ID']
        passwd = args['passwd']

        return serverDAO.insertUser(id, passwd)


api.add_resource(Login, '/login')
api.add_resource(Getuser, '/getuser')
api.add_resource(Insertuser, '/insertuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # push
    # app.run(debug=True)  # local test
