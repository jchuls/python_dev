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
sys.stdout = open(r'C:\Users\youn\CJS\CJS_Output_' + dt.last_mm + '.txt','w')

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
    query = "SELECT dt_sal,	no_pos,	no_rcp,	cd_byr,	amt_sale,amt_notax,	amt_tax,amt_vat,amt_aprv_pnt,amt_cash,amt_cdt,amt_crcard,amt_decard,amt_pbill,amt_ebill,amt_exc,amt_etc,amt_use_pnt,amt_use_ok,	amt_use_etc,amt_dc_cut,	amt_dc_pum,	amt_dc_stot,amt_dc_cpn,	amt_tsale,amt_prft,	amt_pay,amt_change,	cd_swn,	ymd_sale,amt_rcp_byr,ban_dt_sal,ban_no_pos,	ban_no_rcp,	knd_ban,knd_rcp FROM slpossjk WHERE MID(dt_sal, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('CJS_' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\CJS\CJS_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\CJS\CJS_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fc = open(r'C:\Users\youn\CJS\CJS_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fc)

for row in csvReader:
    moi_idx = (row[0])
    sales_date = (row[1])
    pos_no = (row[2])
    rcp_no = (row[3])
    member_no = (row[4])
    sales_amt = (row[5])
    taxfree_amt = (row[6])
    tax_amt = (row[7])
    vat = (row[8])
    aprv_point = (row[9])
    cash = (row[10])
    miss = (row[11])
    credit_card = (row[12])
    check_card = (row[13])
    pbill_amt = (row[14])
    ebill_amt = (row[15])
    exc_amt = (row[16])
    etc_amt = (row[17])
    use_point = (row[18])
    okcashbag_use = (row[19])
    etc_use = (row[20])
    dc_cut_amt = (row[21])
    dc_unit_amt = (row[22])
    dc_stot_amt = (row[23])
    dc_cpn_amt = (row[24])
    tsale_amt = (row[25])
    benefit_price = (row[26])
    pay_amt = (row[27])
    change_amt = (row[28])
    cd_user = (row[29])
    sale_date = (row[30])
    annual_amt = (row[31])
    refund_date = (row[32])
    refund_pos = (row[33])
    refund_rcp = (row[34])
    refund_type = (row[35])
    rcp_check = (row[36])

    sql = "insert into m_cjsmst (moi_idx, sales_date,pos_no,rcp_no,	member_no,sales_amt,taxfree_amt,tax_amt,vat,aprv_point,cash,miss,credit_card,check_card,pbill_amt,ebill_amt,exc_amt,etc_amt,use_point,okcashbag_use,etc_use,dc_cut_amt,	dc_unit_amt,dc_stot_amt,dc_cpn_amt,	tsale_amt,benefit_price,pay_amt,change_amt,	cd_user,sale_date,annual_amt,refund_date,`refund_pos`,refund_rcp,refund_type,rcp_check) values ('" + str(
        moi_idx) + "',	'" + str(sales_date) + "',	'" + str(pos_no) + "',	'" + str(rcp_no) + "',	'" + str(member_no) + "',	'" + str(sales_amt) + "',	'" + str(taxfree_amt) + "',	'" + str(tax_amt) + "',	'" + str(vat) + "',	'" + str(aprv_point) + "',	'" + str(cash) + "',	'" + str(miss) + "',	'" + str(credit_card) + "',	'" + str(check_card) + "',	'" + str(pbill_amt) + "',	'" + str(ebill_amt) + "',	'" + str(
        exc_amt) + "',	'" + str(etc_amt) + "',	'" + str(use_point) + "',	'" + str(okcashbag_use) + "',	'" + str(etc_use) + "',	'" + str(dc_cut_amt) + "',	'" + str(dc_unit_amt) + "',	'" + str(dc_stot_amt) + "',	'" + str(dc_cpn_amt) + "',	'" + str(tsale_amt) + "',	'" + str(benefit_price) + "',	'" + str(pay_amt) + "',	'" + str(change_amt) + "',	'" + str(cd_user) + "',	'" + str(sale_date) + "',	'" + str(
        annual_amt) + "','" + str(refund_date) + "','" + str(refund_pos) + "','" + str(refund_rcp) + "','" + str(refund_type) + "',	'" + str(rcp_check) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_cjsmst;"

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fc.close()

rowcount = 0

for row in open(r'C:\Users\youn\CJS\CJS_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\CJS\CJS_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\CJS')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\CJS\CJS_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_cjs_log (Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()