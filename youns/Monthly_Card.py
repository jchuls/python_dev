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
sys.stdout = open(r'C:\Users\youn\Card\Card_Output_' + dt.last_mm + '.csv','w')

now = datetime.datetime.now()

start_time = timeit.default_timer()  # 시작 시간 체크

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
    query = "SELECT key_date,key_seq,dt_sal,no_pos,	no_rcp,	cd_crd,	nm_crd,	cd_jnp,	nm_jnp,	no_card,knd_qry,knd_sal,knd_pass,dt_pass,no_pass,dt_pass_org,no_pass_org,cd_swn,amt_sale,mon_halbu,	pnt_ok,	pnt_use_ok,	cd_cst,	no_trm,	no_uniq,remark,	cd_byr FROM slcrdsal WHERE MID(dt_sal, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('card' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\card\card_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\card\card_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

fc = open(r'C:\Users\youn\card\card' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fc)

for row in csvReader:
    moi_idx = (row[0])
    ap_date = (row[1])
    ap_seq = (row[2])
    sales_date = (row[3])
    pos_no = (row[4])
    rcp_no = (row[5])
    cd_code = (row[6])
    cd_name = (row[7])
    cd_jcode = (row[8])
    cd_jname = (row[9])
    cd_no = (row[10])
    ap_dv = (row[11])
    ap_tg = (row[12])
    ap_tp = (row[13])
    ap_re = (row[14])
    ap_no = (row[15])
    c_date = (row[16])
    c_no = (row[17])
    c_ow = (row[18])
    amt_sale = (row[19])
    pay_type = (row[20])
    ok_pt = (row[21])
    ok_pt_use = (row[22])
    cst_code = (row[23])
    trm_no = (row[24])
    uniq_no = (row[25])
    etc = (row[26])
    byr_no = (row[27])

    sql = "insert into m_cardmst (moi_idx,	ap_date,ap_seq,	sales_date,	pos_no,	rcp_no,	cd_code,cd_name,cd_jcode,cd_jname,cd_no,ap_dv,ap_tg,ap_tp,ap_re,ap_no,c_date,c_no,c_ow,	amt_sale,pay_type,ok_pt,ok_pt_use,cst_code,	trm_no,	uniq_no,etc,byr_no) values ('" + str(
        moi_idx) + "','" + str(ap_date) + "','" + str(ap_seq) + "',	'" + str(sales_date) + "',	'" + str(pos_no) + "','" + str(rcp_no) + "','" + str(cd_code) + "',	'" + str(cd_name) + "',	'" + str(cd_jcode) + "','" + str(cd_jname) + "','" + str(cd_no) + "','" + str(
        ap_dv) + "','" + str(ap_tg) + "','" + str(ap_tp) + "','" + str(ap_re) + "','" + str(ap_no) + "','" + str(c_date) + "','" + str(c_no) + "','" + str(c_ow) + "','" + str(amt_sale) + "',	'" + str(pay_type) + "','" + str(ok_pt) + "','" + str(
        ok_pt_use) + "','" + str(cst_code) + "','" + str(trm_no) + "','" + str(uniq_no) + "','" + str(etc) + "','" + str(byr_no) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_cardmst;"

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fc.close()

rowcount = 0

for row in open(r'C:\Users\youn\card\card_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\card\card_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\card')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()
terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\card\card_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_card_log (Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()