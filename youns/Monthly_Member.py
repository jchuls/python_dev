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
import re


#시간기록
sys.stdout = open(r'C:\Users\youn\Member\Member_output_' + dt.last_mm + '.csv','w')

now = datetime.datetime.now()

start_time = timeit.default_timer()  # 시작 시간 체크

#DB연결
mart_info_query = "select * from m_office_info where Moi_dataflag ='Y' AND moi_data_type='DB';"

mart_info_result = dbfun.select(mart_info_query)

for mdata in mart_info_result:
    lnfo = {
        "db": mdata['moi_database'],
        "host" : mdata['moi_serverip'],
        "user": mdata['moi_userid'],
        "passwd": mdata['moi_data_pwd'],
        "port": int(mdata['moi_data_port']),
        "charset": mdata['moi_charset']
        }

    conn = pymysql.connect(host=mdata['moi_serverip'],port=lnfo['port'],user=mdata['moi_userid'],password=mdata['moi_data_pwd'],db=mdata['moi_database'],charset=mdata['moi_charset'])
    moi = mdata['mai_Company_num']

    #CSV 저장
    query = "SELECT B.no_saup, A.cd_byr,A.nm_byr,A.dt_birth,A.knd_grd,A.ds_abc,A.nm_saup,A.nm_chip,A.nm_ut,A.day_mis,A.no_zip,A.addr_dtl1,A.addr_dtl2,A.knd_cash,A.pnt_aprv,A.pnt_use,A.pnt_use_able,A.amt_mis,A.dt_gaip,A.knd_sms,A.knd_mail,A.knd_del,A.ymd_last,A.ymd_chg,A.addr_dtl1_saup,A.addr_dtl2_saup FROM msbyrmst A, msshpmst B WHERE MID(A.ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('Member_' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\Member\Member_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\Member\Member_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fm = open(r'C:\Users\youn\Member\Member_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fm)

for row in csvReader:
    moi_idx = (row[0])
    saup_code = (row[1])
    member_code = (row[2])
    member_name = (row[3])
    birthday = (row[4])
    member_grade = (row[5])
    group = (row[6])
    cp_name = (row[7])
    owner = (row[8])
    store_type = (row[9])
    payday = (row[10])
    zip_code = (row[11])
    addr1 = (row[12])
    addr2 = (row[13])
    refund_cash = (row[14])
    aprv_point_sum = (row[15])
    use_point_sum = (row[16])
    usable_point = (row[17])
    amt_miss = (row[18])
    join_date = (row[19])
    sms_check = (row[20])
    mail_check = (row[21])
    status = (row[22])
    last_day = (row[23])
    change_date = (row[24])
    cp_addr1 = (row[25])
    cp_addr2 = (row[26])

    sql = "insert into m_byrmst (moi_idx, saup_code,member_code,member_name, `birthday`, member_grade, `group`, cp_name, `owner`, store_type, payday, `zip_code`, `addr1`, `addr2`, refund_cash, aprv_point_sum, use_point_sum, usable_point, amt_miss, join_date, sms_check, mail_check, `status`, `last_day`, change_date,cp_addr1,cp_addr2) values ('" + str(
        moi_idx) + "', '" + str(saup_code) + "','" + str(member_code) + "',	'" + str(member_name) + "',	'" + str(birthday) + "','" + str(member_grade) + "','" + str(group) + "','" + str(cp_name) + "','" + str(owner) + "','" + str(store_type) + "',	'" + str(payday) + "',	'" + re.sub('[)(+\\\\]'," ",str(zip_code)) + "','" + re.sub("'","",str(addr1)) + "','" + str(addr2) + "','" + str(refund_cash) + "',	'" + str(
        aprv_point_sum) + "',	'" + str(use_point_sum) + "','" + str(usable_point) + "','" + str(amt_miss) + "','" + str(join_date) + "','" + str(sms_check) + "','" + str(mail_check) + "','" + str(status) + "',	'" + str(last_day) + "','" + str(change_date) + "',	'" + str(cp_addr1) + "','" + str(cp_addr2) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_byrmst WHERE MID(change_date, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fm.close()

rowcount = 0

for row in open(r'C:\Users\youn\Member\Member_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1


if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\Member\Member_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\Member')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\Member\Member_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_member_log(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()