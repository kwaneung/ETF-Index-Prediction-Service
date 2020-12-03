FROM python

COPY ./server.py server.py
COPY ./userDAO.py userDAO.py
COPY ./service.py service.py

RUN pip install flask

RUN pip install flask-restful

RUN pip install pymysql

EXPOSE 8000

CMD python server.py