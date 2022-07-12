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
sys.stdout = open(r'C:\Users\youn\Puc\Puc_output_' + dt.last_mm + '.csv','w')

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
    query = "SELECT dt_puc,no_puc,no_seq,cd_bar,cd_cst,	qty_puc,pr_puc_buy,	amt_sec_1,amt_sec_2,pr_puc_vat,	pr_amt_notax,pr_puc_amt,pr_pum_buy,	pr_pum_sale,pr_puc_sale,pr_sal_amt,	knd_puc_dc,	amt_puc_dc,	pr_puc_notax,qty_dum,ymd_reg,ymd_chg FROM pcpucdtl WHERE MID(dt_puc, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('Puc' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\Puc\Puc_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\Puc\Puc_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fp = open(r'C:\Users\youn\Puc\Puc_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fp)

for row in csvReader:
    moi_idx = (row[0])
    puc_date = (row[1])
    puc_no = (row[2])
    puc_seq = (row[3])
    barcode = (row[4])
    cst_code = (row[5])
    puc_qty = (row[6])
    puc_pr = (row[7])
    amt_sec_1 = (row[8])
    amt_sec_2 = (row[9])
    puc_vat = (row[10])
    pr_notax = (row[11])
    puc_amt = (row[12])
    b_puc_pr = (row[13])
    b_sale_pr = (row[14])
    puc_sale_pr = (row[15])
    sale_pr = (row[16])
    puc_dv = (row[17])
    puc_dc = (row[18])
    puc_notax_pr = (row[19])
    dum = (row[20])
    reg_date = (row[21])
    chg_date = (row[22])

    sql = "insert into m_pucmst (moi_idx,puc_date,puc_no,puc_seq,barcode,cst_code,puc_qty,puc_pr,amt_sec_1,	amt_sec_2,	puc_vat,pr_notax,puc_amt,b_puc_pr,b_sale_pr,puc_sale_pr,sale_pr,puc_dv,	puc_dc,	puc_notax_pr,dum,reg_date,chg_date) values ('" + str(
        moi_idx) + "',	'" + str(puc_date) + "','" + str(puc_no) + "','" + str(puc_seq) + "','" + str(barcode) + "','" + str(cst_code) + "','" + str(puc_qty) + "',	'" + str(puc_pr) + "',	'" + str(amt_sec_1) + "','" + str(
        amt_sec_2) + "','" + str(puc_vat) + "',	'" + str(pr_notax) + "','" + str(puc_amt) + "',	'" + str(b_puc_pr) + "','" + str(b_sale_pr) + "','" + str(puc_sale_pr) + "','" + str(sale_pr) + "',	'" + str(puc_dv) + "',	'" + str(
        puc_dc) + "','" + str(puc_notax_pr) + "','" + str(dum) + "','" + str(reg_date) + "','" + str(chg_date) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_pucmst WHERE MID(puc_date, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fp.close()

rowcount = 0

for row in open(r'C:\Users\youn\Puc\Puc_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1


if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\Puc\Puc_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\Puc')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\Puc\Puc_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_puc_log(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()