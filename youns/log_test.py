import dbconfun as dbfun
import pymysql
import pandas as pd
import os
import Date as dt
import timeit
import datetime
import csv
import shutil
import sys


#시간기록
sys.stdout = open(r'C:\Users\youn\test\test_output_' + dt.last_mm + '.csv','w')

now = datetime.datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")

start_time = timeit.default_timer()  # 시작 시간 체크

#DB연결
mart_info_query = "select * from m_office_info where Moi_dataflag ='Y' AND moi_data_type='DB'"

mart_info_result = dbfun.select(mart_info_query)

for mdata in mart_info_result:
    lnfo = {
        "db": mdata['moi_database'],
        "host": mdata['moi_serverip'],
        "user": mdata['moi_userid'],
        "passwd": mdata['moi_data_pwd'],
        "port": int(mdata['moi_data_port']),
        "charset": mdata['moi_charset']
        }

    conn = pymysql.connect(host=mdata['moi_serverip'],port=lnfo['port'],user=mdata['moi_userid'],password=mdata['moi_data_pwd'],db=mdata['moi_database'],charset=mdata['moi_charset'])
    moi = mdata['mai_Company_num']

    #CSV 저장
    query = "SELECT B.no_saup,A.ryucod1,A.ryucod2,A.ryucod3,replace(A.ryunam, '\\\\', ''),A.knd_del,A.ymd_reg, A.ymd_chg FROM msryumst A, msshpmst B WHERE MID(A.ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('Category_test_' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\Category\Category_test_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\Category\Category_test_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fc = open(r'C:\Users\youn\Category\Category_test_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fc)

for row in csvReader:
    moi_idx = (row[0])
    saup_code = (row[1])
    attr1 = (row[2])
    attr2 = (row[3])
    attr3 = (row[4])
    attr_name = (row[5])
    del_check = (row[6])
    reg_date = (row[7])
    ymd_chg = (row[8])

    sql = "insert into m_attmst_test (moi_idx, saup_code,attr1, attr2, attr3, attr_name, del_check, reg_date,ymd_chg) values ('" + str(
        moi_idx) + "','" + str(saup_code) + "', '" + str(attr1) + "', '" + str(attr2) + "', '" + str(attr3) + "', '" + str(
        attr_name) + "', '" + str(del_check) + "', '" + str(reg_date) + "', '" + str(ymd_chg) + "' );"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_attmst_test WHERE MID(ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fc.close()

rowcount = 0

for row in open(r'C:\Users\youn\Category\Category_test_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\Category\Category_test_' + dt.last_mm + '.csv', r'C:\Users\youn\test')

rot = datetime.datetime.now()
ckb = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

lt = datetime.datetime.now()
end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\test\test_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

    sql_l = "insert into m_test_att(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()