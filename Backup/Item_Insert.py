
import csv
import Query as q
import re

# CSV 파일 경로
f45 = open(r'C:\Users\youn\Item\Item_Cheonahn.csv',encoding='utf-8-sig')
csvReader45 = csv.reader(f45)

for row in csvReader45:
    saup_code = (row[0])
    barcode = (row[1])
    bar_desc = (row[2])
    bar_spec = (row[3])
    bar_key = (row[4])
    attr1 = (row[5])
    attr2 = (row[6])
    attr3 = (row[7])
    grc_code = (row[8])
    buy_price_cen = (row[9])
    buy_price = (row[10])
    sale_price = (row[11])
    benefit_rate = (row[12])
    bar_unit_size = (row[13])
    bar_size = (row[14])
    dc_check = (row[15])
    cpn_check = (row[16])
    mini_order = (row[17])
    mini_stk = (row[18])
    point_rate = (row[19])
    mrgsal_rate = (row[20])
    reg_date = (row[21])
    ymd_chg = (row[22])
    limit_qty = (row[23])
    sale_qty = (row[24])
    dc_start_date = (row[25])
    dc_end_date = (row[26])
    bar_valid_date = (row[27])

    sql14 = "insert into m_itemmst (saup_code,barcode,bar_desc,bar_spec,bar_key,attr1,attr2,attr3,grc_code,buy_price_cen,	buy_price,sale_price,benefit_rate,bar_unit_size,bar_size,dc_check,cpn_check,mini_order,	mini_stk,point_rate,mrgsal_rate,reg_date,ymd_chg,limit_qty,sale_qty,dc_start_date,dc_end_date,bar_valid_date) values ('" + str(
            saup_code) + "',	'" + re.sub("'"," ",str(barcode)) + "', '" + re.sub("'","''",str(bar_desc)) + "',	'" + re.sub("'","''",str(bar_spec)) + "',	'" + str(bar_key) + "',	'" + str(
        attr1) + "',	'" + str(attr2) + "',	'" + str(attr3) + "',	'" + str(grc_code) + "',	'" + str(
        buy_price_cen) + "',	'" + str(buy_price) + "',	'" + str(sale_price) + "',	'" + str(
        benefit_rate) + "',	'" + str(bar_unit_size) + "',	'" + str(bar_size) + "',	'" + str(
        dc_check) + "',	'" + str(cpn_check) + "',	'" + str(mini_order) + "',	'" + str(
        mini_stk) + "',	'" + str(point_rate) + "',	'" + str(mrgsal_rate) + "',	'" + str(
        reg_date) + "',	'" + str(ymd_chg) + "',	'" + str(limit_qty) + "',	'" + str(sale_qty) + "',	'" + str(
        dc_start_date) + "',	'" + str(dc_end_date) + "',	'" + str(bar_valid_date) + "');"

    q.cursor14.execute(sql14)


f46 = open(r'C:\Users\youn\Item\Item_Geumchon.csv',encoding='utf-8-sig')
csvReader46 = csv.reader(f46)

for row in csvReader46:
    saup_code = (row[0])
    barcode = (row[1])
    bar_desc = (row[2])
    bar_spec = (row[3])
    bar_key = (row[4])
    attr1 = (row[5])
    attr2 = (row[6])
    attr3 = (row[7])
    grc_code = (row[8])
    buy_price_cen = (row[9])
    buy_price = (row[10])
    sale_price = (row[11])
    benefit_rate = (row[12])
    bar_unit_size = (row[13])
    bar_size = (row[14])
    dc_check = (row[15])
    cpn_check = (row[16])
    mini_order = (row[17])
    mini_stk = (row[18])
    point_rate = (row[19])
    mrgsal_rate = (row[20])
    reg_date = (row[21])
    ymd_chg = (row[22])
    limit_qty = (row[23])
    sale_qty = (row[24])
    dc_start_date = (row[25])
    dc_end_date = (row[26])
    bar_valid_date = (row[27])

    sql14 = "insert into m_itemmst (saup_code,barcode,bar_desc,bar_spec,bar_key,attr1,attr2,attr3,grc_code,buy_price_cen,	buy_price,sale_price,benefit_rate,bar_unit_size,bar_size,dc_check,cpn_check,mini_order,	mini_stk,point_rate,mrgsal_rate,reg_date,ymd_chg,limit_qty,sale_qty,dc_start_date,dc_end_date,bar_valid_date) values ('" + str(
            saup_code) + "',	'" + str(barcode) + "', '" + re.sub("'","''",str(bar_desc)) + "',	'" + re.sub("'","''",str(bar_spec)) + "',	'" + str(bar_key) + "',	'" + str(
        attr1) + "',	'" + str(attr2) + "',	'" + str(attr3) + "',	'" + str(grc_code) + "',	'" + str(
        buy_price_cen) + "',	'" + str(buy_price) + "',	'" + str(sale_price) + "',	'" + str(
        benefit_rate) + "',	'" + str(bar_unit_size) + "',	'" + str(bar_size) + "',	'" + str(
        dc_check) + "',	'" + str(cpn_check) + "',	'" + str(mini_order) + "',	'" + str(
        mini_stk) + "',	'" + str(point_rate) + "',	'" + str(mrgsal_rate) + "',	'" + str(
        reg_date) + "',	'" + str(ymd_chg) + "',	'" + str(limit_qty) + "',	'" + str(sale_qty) + "',	'" + str(
        dc_start_date) + "',	'" + str(dc_end_date) + "',	'" + str(bar_valid_date) + "');"

    q.cursor14.execute(sql14)


f47 = open(r'C:\Users\youn\Item\Item_Hwagok.csv',encoding='utf-8-sig')
csvReader47 = csv.reader(f47)

for row in csvReader47:
    saup_code = (row[0])
    barcode = (row[1])
    bar_desc = (row[2])
    bar_spec = (row[3])
    bar_key = (row[4])
    attr1 = (row[5])
    attr2 = (row[6])
    attr3 = (row[7])
    grc_code = (row[8])
    buy_price_cen = (row[9])
    buy_price = (row[10])
    sale_price = (row[11])
    benefit_rate = (row[12])
    bar_unit_size = (row[13])
    bar_size = (row[14])
    dc_check = (row[15])
    cpn_check = (row[16])
    mini_order = (row[17])
    mini_stk = (row[18])
    point_rate = (row[19])
    mrgsal_rate = (row[20])
    reg_date = (row[21])
    ymd_chg = (row[22])
    limit_qty = (row[23])
    sale_qty = (row[24])
    dc_start_date = (row[25])
    dc_end_date = (row[26])
    bar_valid_date = (row[27])

    sql14 = "insert into m_itemmst (saup_code,barcode,bar_desc,bar_spec,bar_key,attr1,attr2,attr3,grc_code,buy_price_cen,	buy_price,sale_price,benefit_rate,bar_unit_size,bar_size,dc_check,cpn_check,mini_order,	mini_stk,point_rate,mrgsal_rate,reg_date,ymd_chg,limit_qty,sale_qty,dc_start_date,dc_end_date,bar_valid_date) values ('" + str(
            saup_code) + "',	'" + str(barcode) + "', '" + re.sub("'","''",str(bar_desc)) + "',	'" + re.sub("'","''",str(bar_spec)) + "',	'" + str(bar_key) + "',	'" + str(
        attr1) + "',	'" + str(attr2) + "',	'" + str(attr3) + "',	'" + str(grc_code) + "',	'" + str(
        buy_price_cen) + "',	'" + str(buy_price) + "',	'" + str(sale_price) + "',	'" + str(
        benefit_rate) + "',	'" + str(bar_unit_size) + "',	'" + str(bar_size) + "',	'" + str(
        dc_check) + "',	'" + str(cpn_check) + "',	'" + str(mini_order) + "',	'" + str(
        mini_stk) + "',	'" + str(point_rate) + "',	'" + str(mrgsal_rate) + "',	'" + str(
        reg_date) + "',	'" + str(ymd_chg) + "',	'" + str(limit_qty) + "',	'" + str(sale_qty) + "',	'" + str(
        dc_start_date) + "',	'" + str(dc_end_date) + "',	'" + str(bar_valid_date) + "');"

    q.cursor14.execute(sql14)
