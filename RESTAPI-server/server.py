from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import pymysql
import serverDAO

app = Flask(__name__)
api = Api(app)

connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                          db='ETFIPS', charset='utf8')

cur = connect.cursor()


class login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ID', type=str)
        parser.add_argument('passwd', type=str)
        args = parser.parse_args()

        sql = "select * from user"
        cur.execute(sql)
        rows = cur.fetchall()  # id, name, passwd, money, max_prft_pct, min_loss_pct, prft_from_prev_mon, loss_from_prev_mon

        ID = args['ID']
        passwd = args['passwd']
        print('Request ID : ' + ID)
        print('Request passwd : ' + passwd)

        rows = [i[1:3] for i in rows]
        print(rows)

        if (ID, passwd) in rows:
            print('Result : True')
            return {'result': 'true'}
        else:
            print('False')
            return {'result': 'false'}


class getuser(Resource):
    def get(self):
        return serverDAO.getUser()


api.add_resource(login, '/login')
api.add_resource(getuser, '/getuser')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # push
    # app.run(debug=True)  # local test
