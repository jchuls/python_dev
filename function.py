import pymysql

def select_query(con,query,debug = 0):
    curs = con.cursor(pymysql.cursors.DictCursor)
    curs.execute(query)
    # 데이터 결과를 만든다.
    result = curs.fetchall()

    return result