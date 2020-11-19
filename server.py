from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import pymysql

app = Flask(__name__)
api = Api(app)

connect = pymysql.connect(host='192.168.0.40', user='root', password='0000',
                          db='kwaneung', charset='utf8')

cur = connect.cursor()


class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        sql = "select * from user"
        cur.execute(sql)
        rows = cur.fetchall()

        ID = args['ID']
        passwd = args['passwd']
        print('Request ID : ' + ID)
        print('Request passwd : ' + passwd)

        if (ID, passwd) in rows:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}


api.add_resource(RegistUser, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)