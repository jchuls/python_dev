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
sys.stdout = open(r'C:\Users\youn\sales\sales_output_' + dt.last_mm + '.csv','w')

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
    query = "SELECT B.no_saup, A.dt_sal,A.no_pos,A.no_rcp,A.no_seq,A.cd_bar,A.qty_sale,A.pr_pos_sale,A.pr_sale,A.pr_dc_evt,A.pr_dc_pos,A.amt_sale,A.pr_buy,A.pr_buy_dc,A.rt_prft,A.amt_prft,A.amt_bot,A.qty_wet,A.no_dscseq,A.amt_dc_evt,A.amt_pnt,A.amt_tsale,A.knd_change,A.knd_dsc_bas,A.amt_dsc,A.knd_bar,A.rt_susu,A.rt_card_susu,A.rt_pnt_susu,A.amt_card,A.amt_point,A.cd_cst,A.amt_vat,A.ymd_sale FROM slpospum A, msshpmst B WHERE MID(A.dt_sal, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('Sales_' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\Sales\Sales_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\Sales\Sales_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fs = open(r'C:\Users\youn\Sales\Sales_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fs)

for row in csvReader:
    moi_idx = (row[0])
    saup_code = (row[1])
    sales_date = (row[2])
    pos_no = (row[3])
    rcp_no = (row[4])
    no_seq = (row[5])
    barcode = (row[6])
    sale_qty = (row[7])
    pos_sale_price = (row[8])
    sale_price = (row[9])
    dc_price = (row[10])
    event_price = (row[11])
    sale_amt = (row[12])
    buy_price = (row[13])
    dc_buy_price = (row[14])
    benefit_rate = (row[15])
    benefit_amt = (row[16])
    bot_price = (row[17])
    weight = (row[18])
    dc_no = (row[19])
    event_dc = (row[20])
    point_amt = (row[21])
    tsales_amt = (row[22])
    price_change_check = (row[23])
    dc_check = (row[24])
    dc_amt = (row[25])
    bar_check = (row[26])
    sale_comis_rate = (row[27])
    card_comis_rate = (row[28])
    point_comis_rate = (row[29])
    card_sale_amt = (row[30])
    point_sale_amt = (row[31])
    cst_code = (row[32])
    vat = (row[33])
    sale_date = (row[34])

    sql = "insert into m_rawmst (moi_idx, saup_code,sales_date,pos_no,rcp_no,no_seq,	barcode,sale_qty,pos_sale_price,sale_price,	dc_price,event_price,sale_amt,buy_price,dc_buy_price,benefit_rate,benefit_amt,bot_price,weight,	dc_no,event_dc,point_amt,tsales_amt,price_change_check,	dc_check,dc_amt,bar_check,sale_comis_rate,card_comis_rate,point_comis_rate,card_sale_amt,point_sale_amt,cst_code,vat,`sale_date`) values ('" + str(
        moi_idx) + "','" + str(saup_code) + "','" + str(sales_date) + "',	'" + str(pos_no) + "',	'" + str(rcp_no) + "',	'" + str(no_seq) + "',	'" + str(
        barcode) + "',	'" + str(sale_qty) + "',	'" + str(pos_sale_price) + "',	'" + str(
        sale_price) + "',	'" + str(dc_price) + "',	'" + str(event_price) + "',	'" + str(
        sale_amt) + "',	'" + str(buy_price) + "',	'" + str(
        dc_buy_price) + "',	'" + str(benefit_rate) + "',	'" + str(benefit_amt) + "',	'" + str(
        bot_price) + "',	'" + str(weight) + "',	'" + str(dc_no) + "',	'" + str(event_dc) + "',	'" + str(
        point_amt) + "',	'" + str(tsales_amt) + "',	'" + str(price_change_check) + "',	'" + str(
        dc_check) + "',	'" + str(
        dc_amt) + "',	'" + str(bar_check) + "',	'" + str(sale_comis_rate) + "',	'" + str(
        card_comis_rate) + "',	'" + str(point_comis_rate) + "',	'" + str(card_sale_amt) + "',	'" + str(
        point_sale_amt) + "',	'" + str(cst_code) + "',	'" + str(vat) + "',	'" + str(sale_date) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_rawmst WHERE MID(sales_date, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fs.close()

rowcount = 0

for row in open(r'C:\Users\youn\sales\sales_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\sales\sales_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\sales')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\sales\sales_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_sales_log(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()