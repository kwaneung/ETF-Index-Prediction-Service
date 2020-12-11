# ETF-Index-Prediction-Service
ETF Index Prediction Service


# Infra
k8s-master-01\
k8s-worker-01\
k8s-worker-02\
 -> 쿠버네티스 클러스터\
db-mariadb-01\
 -> mariadb\
jkns-server-01\
 -> Jenkins 서버
 
 
깃 푸시를 하게되면 젠킨스 서버에서 웹훅으로 가져와 쉘 수행
 
 
추후 별도 서버들은 모두 쿠버네티스 클러스터 안에 Pod로 마이그레이션 할 예정


# Rest API Server

사용 라이브러리 : Flask, flask_restful, pymysql

server.py : 메인 서버 \
user_DAO.py : 사용자 DB 처리 \
user_service.py : 로직 처리 

/login
- post : login {id, passwd}

/user
- post : insert user {id, passwd}
- patch : update user {id, passwd} password 변경
- get : get user
- delete : delete user {id}