import pymysql

connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                          db='ETFIPS', charset='utf8')


def commit():
    cur = connect.cursor()
    sql = "commit"
    cur.execute(sql)
    return


def getUser():
    cur = connect.cursor()

    sql = "select * from user"
    cur.execute(sql)
    return cur.fetchall()


def insertUser(id, password):
    cur = connect.cursor()
    print(id)
    print(password)

    sql = "insert into user values(%s,%s)"
    cur.execute(sql, (id, password))
    commit()

    return


def setUser(id, password):
    # 존재하면 update, 없으면 insert
    # id, password
    cur = connect.cursor()

    sql = "update user set password=%s where id=%s"
    cur.execute(sql, password, id)
    commit()

    return


def deleteUser(id):
    cur = connect.cursor()

    sql = "delete from user where id=%s"
    cur.execute(sql, id)
    commit()

    return


if __name__ == '__main__':
    # insertUser('kwaneung3', '1q2w3e4r')
    # deleteUser('kwaneung2')
    print(getUser())
