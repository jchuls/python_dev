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
sys.stdout = open(r'C:\Users\youn\item\item_output_' + dt.last_mm + '.csv','w')

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
    query = "SELECT B.no_saup, A.cd_bar,A.nm_bar,A.spec_bar,A.nm_key,A.cd_ryu1,A.cd_ryu2,A.cd_ryu3,A.cd_cst,A.pr_buy_cen,A.pr_buy,A.pr_sale,A.rt_prft,A.siz_unit_bar,A.siz_tot_bar,A.knd_dc,A.knd_cpn,A.qty_min_ord,A.qty_min_stk,A.rt_point,A.rt_mrgsal,A.ymd_reg,A.ymd_chg,A.e_qty_limit,A.e_qty_dsc_sale,A.e_dt_start,A.e_dt_end,A.dt_valid_pum FROM mspummst A, msshpmst B WHERE MID(A.ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

    cursor_t = conn.cursor()
    query_r = cursor_t.execute(query)
    result1 = cursor_t.fetchall()
    result_t = pd.DataFrame(result1)
    result_a = result_t.insert(0,'moi_idx',moi)

    if not os.path.exists('Item_' + dt.last_mm + '.csv'):
        result_t.to_csv(r'C:\Users\youn\Item\Item_' + dt.last_mm + '.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    else:
        result_t.to_csv(r'C:\Users\youn\Item\Item_' + dt.last_mm + '.csv', index=False, mode='w', encoding='utf-8-sig', header=False)

csv_t = datetime.datetime.now()

#CSV Insert
fI = open(r'C:\Users\youn\Item\Item_' + dt.last_mm + '.csv',encoding='utf-8-sig')
csvReader = csv.reader(fI)

for row in csvReader:
    moi_idx = (row[0])
    saup_code = (row[1])
    barcode = (row[2])
    bar_desc = (row[3])
    bar_spec = (row[4])
    bar_key = (row[5])
    attr1 = (row[6])
    attr2 = (row[7])
    attr3 = (row[8])
    grc_code = (row[9])
    buy_price_cen = (row[10])
    buy_price = (row[11])
    sale_price = (row[12])
    benefit_rate = (row[13])
    bar_unit_size = (row[14])
    bar_size = (row[15])
    dc_check = (row[16])
    cpn_check = (row[17])
    mini_order = (row[18])
    mini_stk = (row[19])
    point_rate = (row[20])
    mrgsal_rate = (row[21])
    reg_date = (row[22])
    ymd_chg = (row[23])
    limit_qty = (row[24])
    sale_qty = (row[25])
    dc_start_date = (row[26])
    dc_end_date = (row[27])
    bar_valid_date = (row[28])

    sql = "insert into m_itemmst (moi_idx,saup_code,barcode,bar_desc,bar_spec,bar_key,attr1,attr2,attr3,grc_code,buy_price_cen,	buy_price,sale_price,benefit_rate,bar_unit_size,bar_size,dc_check,cpn_check,mini_order,	mini_stk,point_rate,mrgsal_rate,reg_date,ymd_chg,limit_qty,sale_qty,dc_start_date,dc_end_date,bar_valid_date) values ('" + str(
        moi_idx) + "','" + str(saup_code) + "',	'" + str(barcode) + "', '" + re.sub("'","''",str(bar_desc)) + "',	'" + re.sub("'","''",str(bar_spec)) + "',	'" + str(bar_key) + "',	'" + str(
        attr1) + "',	'" + str(attr2) + "',	'" + str(attr3) + "',	'" + str(grc_code) + "',	'" + str(
        buy_price_cen) + "',	'" + str(buy_price) + "',	'" + str(sale_price) + "',	'" + str(
        benefit_rate) + "',	'" + str(bar_unit_size) + "',	'" + str(bar_size) + "',	'" + str(
        dc_check) + "',	'" + str(cpn_check) + "',	'" + str(mini_order) + "',	'" + str(
        mini_stk) + "',	'" + str(point_rate) + "',	'" + str(mrgsal_rate) + "',	'" + str(
        reg_date) + "',	'" + str(ymd_chg) + "',	'" + str(limit_qty) + "',	'" + str(sale_qty) + "',	'" + str(
        dc_start_date) + "',	'" + str(dc_end_date) + "',	'" + str(bar_valid_date) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql)

inst = datetime.datetime.now()

#작업확인 및 백업
sql_c = "SELECT COUNT(moi_idx) as cnt FROM m_itemmst WHERE MID(ymd_chg, 1, 7) LIKE" '"%' + dt.last_m + '%"'

cursor_c = dbfun.conn.cursor()
cursor_c.execute(sql_c)

result = cursor_c.fetchall()

fI.close()

rowcount = 0

for row in open(r'C:\Users\youn\item\item_' + dt.last_mm + '.csv',encoding='utf-8-sig'):
 rowcount += 1

if result[0][0] == rowcount:
   shutil.move(r'C:\Users\youn\item\item_' + dt.last_mm + '.csv', r'C:\Users\youn\Backup\item')

ckb = datetime.datetime.now()
rot = datetime.datetime.now()

terminate_time = timeit.default_timer()  # 종료 시간 체크

end = datetime.datetime.now()

print("Start date and time : " + now.strftime("%Y-%m-%d %H:%M:%S") + " / CSV 생성 완료 : " + csv_t.strftime("%Y-%m-%d %H:%M:%S") + " / CSV DB Insert 완료 : " + inst.strftime("%Y-%m-%d %H:%M:%S") + " / %f rows Insert 완료 : " % (result[0][0]) + rot.strftime("%Y-%m-%d %H:%M:%S") + " / Inserted row checking and backup 완료 : " + ckb.strftime("%Y-%m-%d %H:%M:%S") + " / End time : " + end.strftime("%Y-%m-%d %H:%M:%S") + " / " + dt.last_m + " 작업 완료 : " "%f초 걸렸습니다." % (terminate_time - start_time))

sys.stdout.close()

#Log 기록
lg = open(r'C:\Users\youn\item\item_output_' + dt.last_mm + '.csv', encoding='cp949')
csvReader_l = csv.reader(lg)

for row in csvReader_l:
    Log = (row[0])

if result[0][0] == rowcount:
    sql_l = "insert into m_item_log(Log) values ('" + str(Log) + "');"

    cursor_s = dbfun.conn.cursor()
    cursor_s.execute(sql_l)

dbfun.conn.close()
