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
sys.stdout = open(r'C:\Users\youn\GRC\GRC_output_' + dt.last_mm + '.csv','w')

now = datetime.datetime.now()

start_time = timeit.default_timer() # 시작 시간 체크

#DB연결
mart_info_query = "select * from m_office_info where Moi_dataflag ='Y' AND moi_data_type='DB'"

mart_info_result = dbfun.select(mart_info_query)

for mdata in mart_info_result:
    lnfo = {
        "db" : mdata['moi_database'],
        "host" : mdata['moi_serverip'],
        "user": mdata['moi_userid'],
        "passwd": mdata['moi_data_pwd'],
        "port" : int(mdata['moi_data_port']),
        "charset": mdata['moi_charset']
        }

    conn = pymysql.connect(host=mdata['moi_serverip'],port=lnfo['port'],user=mdata['moi_userid'],password=mdata['moi_data_pwd'],db=mdata['moi_database'],charset=mdata['moi_charset'])
    moi = mdata['mai_Company_num']

    #CSV 저장
    query = "SELECT B.no_saup, A.cd_cst,A.nm_cst,A.no_saup,A.nm_chip,A.addr_dtl1,A.addr_dtl2,A.no_tel,A.nm_dam,A.no_dam_tel,A.knd_cst,A.upt_cst,A.ymd_trd_start,A.ymd_trd_end,	A.type_app,	A.day_app,	A.knd_trade,A.mrg_basic,A.mrg_sal,A.mrg_card,A.mrg_point,A.mrg_app,	A.mrg_app_dc,A.knd_app,	A.ds_abc,A.day_balju,A.day_ipgo,A.knd_del,A.ymd_reg,A.ymd_chg,A.cd_user,A.week_balju_sun,A.week_balju_mon,A.week_balju_tue,A.week_balju_wed,A.week_balju_thu,A.week_balju_fri,A.week_balju_sat,	A.cd_bank,A.cd_team,A.mrg_logst,A.mrg_minab,A.knd_logst,A.orderno_cst,A.orderno_last,A.orderno_last_log,A.knd_logst_m FROM mscstmst A, msshpmst B WHERE MID(A.ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('GRC' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\GRC\GRC_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\GRC\GRC_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fg = open(r'C:\Users\youn\GRC\GRC_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fg)

for row in csvReader:
    moi_idx = (row[0])
    saup_code = (row[1])
    cst_code = (row[2])
    cst_name = (row[3])
    cst_no = (row[4])
    owner = (row[5])
    addr1 = (row[6])
    addr2 = (row[7])
    tel = (row[8])
    checker_name = (row[9])
    checker_tel = (row[10])
    cst_check = (row[11])
    cst_type = (row[12])
    trd_start_date = (row[13])
    trd_end_date = (row[14])
    app_type = (row[15])
    app_date = (row[16])
    trd_check = (row[17])
    basic_mrg = (row[18])
    sale_mrg = (row[19])
    card_mrg = (row[20])
    point_mrg = (row[21])
    app_rate = (row[21])
    app_dc_rate = (row[23])
    app_check = (row[24])
    group = (row[25])
    order_term = (row[26])
    order_after_day = (row[27])
    trd_stop_check = (row[28])
    reg_date = (row[29])
    change_date = (row[30])
    cd_user = (row[31])
    order_sun = (row[32])
    order_mon = (row[33])
    order_tue = (row[34])
    order_wed = (row[35])
    order_thu = (row[36])
    order_fri = (row[37])
    order_sat = (row[38])
    bank_code = (row[39])
    team_code = (row[40])
    logst_mrg = (row[41])
    miss_rate = (row[42])
    logst_check = (row[43])
    order_no_key = (row[44])
    last_order_no = (row[45])
    logst_last_order_no = (row[46])
    logst_check_no = (row[47])

    sql = "insert into m_grcmst (moi_idx, saup_code,cst_code,cst_name,	cst_no,	`owner`,`addr1`,`addr2`,`tel`,checker_name,checker_tel,cst_check,cst_type,trd_start_date,trd_end_date,app_type,app_date,trd_check,basic_mrg,sale_mrg,card_mrg,point_mrg,app_rate,app_dc_rate,app_check,	`group`,order_term,	order_after_day,trd_stop_check,	reg_date,change_date,cd_user,order_sun,order_mon,order_tue,	order_wed,order_thu,order_fri,order_sat,bank_code,team_code,logst_mrg,miss_rate,logst_check,order_no_key,last_order_no,	logst_last_order_no,logst_check_no) values ('" + str(
        moi_idx) + "','" + str(saup_code) + "','" + str(cst_code) + "','" + str(cst_name) + "','" + str(cst_no) + "','" + str(owner) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(tel) + "','" + str(checker_name) + "','" + str(checker_tel) + "','" + str(
        cst_check) + "','" + str(cst_type) + "','" + str(trd_start_date) + "','" + str(trd_end_date) + "','" + str(app_type) + "','" + str(
        app_date) + "','" + str(trd_check) + "','" + str(basic_mrg) + "','" + str(sale_mrg) + "','" + str(card_mrg) + "','" + str(
        point_mrg) + "','" + str(app_rate) + "','" + str(app_dc_rate) + "','" + str(app_check) + "','" + str(group) + "','" + str(
        order_term) + "','" + str(order_after_day) + "','" + str(trd_stop_check) + "','" + str(reg_date) + "','" + str(change_date) + "','" + str(
        cd_user) + "','" + str(order_sun) + "','" + str(order_mon) + "','" + str(order_tue) + "','" + str(order_wed) + "','" + str(
        order_thu) + "','" + str(order_fri) + "','" + str(order_sat) + "','" + str(bank_code) + "','" + str(team_code) + "','" + str(
        logst_mrg) + "','" + str(miss_rate) + "','" + str(logst_check) + "','" + str(order_no_key) + "','" + str(last_order_no) + "','" + str(
        logst_last_order_no) + "','" + str(logst_check_no) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_grcmst WHERE MID(change_date, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fg.close()

rowcount = 0

for row in open(r'C:\Users\youn\GRC\GRC_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\GRC\GRC_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\GRC')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\GRC\GRC_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_grc_log(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()
