#pip install pymysql
import pymysql
# mariadb연동을 위한 모듈 import


# 컨넥트를 미리 만들어준다.
# 접속할 host, uesr, password, db, 인코딩 입력
connect = pymysql.connect(host='192.168.0.40', user='etfuser', password='1q2w3e4r',
                          db='ETFIPS', charset='utf8')

# 커서 생성
cur = connect.cursor()

# sql문 실행
sql = "select * from user"
cur.execute(sql)

# DB결과를 모두 가져올 때 사용
print("fetchall : 쿼리 결과를 모두 가져올 때")
rows = cur.fetchall()

# 한번에 다 출력
print(rows)
# 원하는 행만 출력
print(rows[0])
# for문으로 출력
for row in rows:
    print(row)
print()

print("fetchone : 쿼리 결과를 한줄만 가져올 때")
cur.execute(sql)

rows = cur.fetchone()
print(rows)

rows = cur.fetchone()
print(rows)

# insert test
# sql = "insert into user values('kwaneung2', '1q2w3e4r')"
#
# cur.execute(sql)
#
# sql = "select * from user"
# cur.execute(sql)
# print(cur.fetchall())

# delete test
# sql = "delete from user where name=%s"
# cur.execute(sql, 'kwaneung3')  # sql, 변수를 ,로 나눠서 나열해주면댐

# commit
sql = "commit"
cur.execute(sql)

# 연결 해제
connect.close()
