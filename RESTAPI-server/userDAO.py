import pymysql
import logging


def dbConnect(host, user, password, db):
    try:
        return pymysql.connect(host, user, password, db, charset='utf8')
    except Exception as e:
        logging.error(e)
        logging.exception(e)
        return False
        raise


def commit(connect):
    cur = connect.cursor()
    sql = """commit"""
    cur.execute(sql)
    return


def getUser():
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    if not connect:
        print("연결 실패")
        return False
    else:
        cur = connect.cursor()
        sql = """select * from user"""
        cur.execute(sql)
        return cur.fetchall()


def insertUser(id, password):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    cur = connect.cursor()
    sql = """insert into user values(%s,%s)"""
    cur.execute(sql, (id, password))
    commit(connect)
    return


def updateUser(id, password):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    cur = connect.cursor()
    sql = """update user set password=%s where id=%s"""
    cur.execute(sql, (password, id))
    commit(connect)
    return


def deleteUser(id):
    connect = dbConnect('192.168.0.40', 'etfuser', '1q2w3e4r', 'ETFIPS')
    cur = connect.cursor()
    sql = """delete from user where id=%s"""
    cur.execute(sql, id)
    commit(connect)
    return


if __name__ == '__main__':
    print("==========getUser==========")
    print(getUser())
    print("==========insertUser==========")
    insertUser('DAOtest', '1q2w3e4r')
    print(getUser())
    print("==========updateUser==========")
    updateUser("DAOtest", "zaq1@WSX")
    print(getUser())
    print("==========deleteUser==========")
    deleteUser('DAOtest')
    print(getUser())
    print("==========getUser==========")
    print(getUser())
