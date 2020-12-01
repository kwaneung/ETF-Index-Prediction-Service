import pymysql


def getUser():
    connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                              db='ETFIPS', charset='utf8')

    cur = connect.cursor()

    sql = "select * from user"
    cur.execute(sql)
    rows = cur.fetchall()

    return rows


def setUser():  # 존재하면 update, 없으면 insert
    connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                              db='ETFIPS', charset='utf8')

    cur = connect.cursor()

    sql = "select * from user"
    cur.execute(sql)
    rows = cur.fetchall()

    return rows


def deleteUser():
    connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                              db='ETFIPS', charset='utf8')

    cur = connect.cursor()

    sql = "select * from user"
    cur.execute(sql)
    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    print(getUser())
