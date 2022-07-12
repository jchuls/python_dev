import sys
from sqlalchemy import true

#DB접속정보
import datetime
import pymysql

lnfo = {
"db" : "mommart",
"host" : "192.168.10.83",
"user":"root",
"passwd":"data!@34",
"port" : 3306,
"charset":"utf8"
}

myconf = lnfo
conn = pymysql.connect(
                    host=myconf['host'],
                    port=myconf['port'],
                    user=myconf['user'],
                    password=myconf['passwd'],
                    db=myconf['db'],
                    charset=myconf['charset'],
                    autocommit=true
                        )

def select(query, debug = 0):
    global conn

    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(query)
    # 데이터 결과를 만든다.
    result = curs.fetchall()

    return result

def merge(query, debug = 0):
    global conn

    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute(query)
    # 쿼리 실행결과를 내보낸다.
    return curs