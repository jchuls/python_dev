
import csv
import Query as q



# CSV 파일 경로
f35 = open(r'C:\Users\youn\Sales\Sales_Cheonahn_06.csv',encoding='utf-8-sig')
csvReader35 = csv.reader(f35)

for row in csvReader35:
    saup_code = (row[0])
    sales_date = (row[1])
    pos_no = (row[2])
    rcp_no = (row[3])
    no_seq = (row[4])
    barcode = (row[5])
    sale_qty = (row[6])
    pos_sale_price = (row[7])
    sale_price = (row[8])
    dc_price = (row[9])
    event_price = (row[10])
    sale_amt = (row[11])
    buy_price = (row[12])
    dc_buy_price = (row[13])
    benefit_rate = (row[14])
    benefit_amt = (row[15])
    bot_price = (row[16])
    weight = (row[17])
    dc_no = (row[18])
    event_dc = (row[19])
    point_amt = (row[20])
    tsales_amt = (row[21])
    price_change_check = (row[22])
    dc_check = (row[23])
    dc_amt = (row[24])
    bar_check = (row[25])
    sale_comis_rate = (row[26])
    card_comis_rate = (row[27])
    point_comis_rate = (row[28])
    card_sale_amt = (row[29])
    point_sale_amt = (row[30])
    cst_code = (row[31])
    vat = (row[32])
    sale_date = (row[33])

    sql13 = "insert into m_rawmst (saup_code,sales_date,pos_no,rcp_no,no_seq,	barcode,sale_qty,pos_sale_price,sale_price,	dc_price,event_price,sale_amt,buy_price,dc_buy_price,benefit_rate,benefit_amt,bot_price,weight,	dc_no,event_dc,point_amt,tsales_amt,price_change_check,	dc_check,dc_amt,bar_check,sale_comis_rate,card_comis_rate,point_comis_rate,card_sale_amt,point_sale_amt,cst_code,vat,`sale_date`) values ('" + str(
        saup_code) + "','" + str(sales_date) + "',	'" + str(pos_no) + "',	'" + str(rcp_no) + "',	'" + str(no_seq) + "',	'" + str(
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

    q.cursor13.execute(sql13)

f36 = open(r'C:\Users\youn\Sales\Sales_Geumchon_06.csv',encoding='utf-8-sig')
csvReader36 = csv.reader(f36)

for row in csvReader36:
    saup_code = (row[0])
    sales_date = (row[1])
    pos_no = (row[2])
    rcp_no = (row[3])
    no_seq = (row[4])
    barcode = (row[5])
    sale_qty = (row[6])
    pos_sale_price = (row[7])
    sale_price = (row[8])
    dc_price = (row[9])
    event_price = (row[10])
    sale_amt = (row[11])
    buy_price = (row[12])
    dc_buy_price = (row[13])
    benefit_rate = (row[14])
    benefit_amt = (row[15])
    bot_price = (row[16])
    weight = (row[17])
    dc_no = (row[18])
    event_dc = (row[19])
    point_amt = (row[20])
    tsales_amt = (row[21])
    price_change_check = (row[22])
    dc_check = (row[23])
    dc_amt = (row[24])
    bar_check = (row[25])
    sale_comis_rate = (row[26])
    card_comis_rate = (row[27])
    point_comis_rate = (row[28])
    card_sale_amt = (row[29])
    point_sale_amt = (row[30])
    cst_code = (row[31])
    vat = (row[32])
    sale_date = (row[33])

    sql13 = "insert into m_rawmst (saup_code,sales_date,pos_no,rcp_no,no_seq,	barcode,sale_qty,pos_sale_price,sale_price,	dc_price,event_price,sale_amt,buy_price,dc_buy_price,benefit_rate,benefit_amt,bot_price,weight,	dc_no,event_dc,point_amt,tsales_amt,price_change_check,	dc_check,dc_amt,bar_check,sale_comis_rate,card_comis_rate,point_comis_rate,card_sale_amt,point_sale_amt,cst_code,vat,`sale_date`) values ('" + str(
        saup_code) + "','" + str(sales_date) + "',	'" + str(pos_no) + "',	'" + str(rcp_no) + "',	'" + str(no_seq) + "',	'" + str(
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

    q.cursor13.execute(sql13)

f37 = open(r'C:\Users\youn\Sales\Sales_Hwagok_06.csv',encoding='utf-8-sig')
csvReader37 = csv.reader(f37)

for row in csvReader37:
    saup_code = (row[0])
    sales_date = (row[1])
    pos_no = (row[2])
    rcp_no = (row[3])
    no_seq = (row[4])
    barcode = (row[5])
    sale_qty = (row[6])
    pos_sale_price = (row[7])
    sale_price = (row[8])
    dc_price = (row[9])
    event_price = (row[10])
    sale_amt = (row[11])
    buy_price = (row[12])
    dc_buy_price = (row[13])
    benefit_rate = (row[14])
    benefit_amt = (row[15])
    bot_price = (row[16])
    weight = (row[17])
    dc_no = (row[18])
    event_dc = (row[19])
    point_amt = (row[20])
    tsales_amt = (row[21])
    price_change_check = (row[22])
    dc_check = (row[23])
    dc_amt = (row[24])
    bar_check = (row[25])
    sale_comis_rate = (row[26])
    card_comis_rate = (row[27])
    point_comis_rate = (row[28])
    card_sale_amt = (row[29])
    point_sale_amt = (row[30])
    cst_code = (row[31])
    vat = (row[32])
    sale_date = (row[33])

    sql13 = "insert into m_rawmst (saup_code,sales_date,pos_no,rcp_no,no_seq,	barcode,sale_qty,pos_sale_price,sale_price,	dc_price,event_price,sale_amt,buy_price,dc_buy_price,benefit_rate,benefit_amt,bot_price,weight,	dc_no,event_dc,point_amt,tsales_amt,price_change_check,	dc_check,dc_amt,bar_check,sale_comis_rate,card_comis_rate,point_comis_rate,card_sale_amt,point_sale_amt,cst_code,vat,`sale_date`) values ('" + str(
        saup_code) + "','" + str(sales_date) + "',	'" + str(pos_no) + "',	'" + str(rcp_no) + "',	'" + str(no_seq) + "',	'" + str(
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

    q.cursor13.execute(sql13)

    print(time.time() - start)

