
import csv
import Query as q

#CSV 파일 경로
f75 = open(r'C:\Users\youn\GRC\GRC_Cheonahn.csv',encoding='utf-8-sig')
csvReader75 = csv.reader(f75)

for row in csvReader75:
    saup_code = (row[0])
    cst_code = (row[1])
    cst_name = (row[2])
    cst_no = (row[3])
    owner = (row[4])
    addr1 = (row[5])
    addr2 = (row[6])
    tel = (row[7])
    checker_name = (row[8])
    checker_tel = (row[9])
    cst_check = (row[10])
    cst_type = (row[11])
    trd_start_date = (row[12])
    trd_end_date = (row[13])
    app_type = (row[14])
    app_date = (row[15])
    trd_check = (row[16])
    basic_mrg = (row[17])
    sale_mrg = (row[18])
    card_mrg = (row[19])
    point_mrg = (row[20])
    app_rate = (row[21])
    app_dc_rate = (row[22])
    app_check = (row[23])
    group = (row[24])
    order_term = (row[25])
    order_after_day = (row[26])
    trd_stop_check = (row[27])
    reg_date = (row[28])
    change_date = (row[29])
    cd_user = (row[30])
    order_sun = (row[31])
    order_mon = (row[32])
    order_tue = (row[33])
    order_wed = (row[34])
    order_thu = (row[35])
    order_fri = (row[36])
    order_sat = (row[37])
    bank_code = (row[38])
    team_code = (row[39])
    logst_mrg = (row[40])
    miss_rate = (row[41])
    logst_check = (row[42])
    order_no_key = (row[43])
    last_order_no = (row[44])
    logst_last_order_no = (row[45])
    logst_check_no = (row[46])

    sql17 = "insert into m_grcmst (saup_code,cst_code,cst_name,	cst_no,	`owner`,`addr1`,`addr2`,`tel`,checker_name,checker_tel,cst_check,cst_type,trd_start_date,trd_end_date,app_type,app_date,trd_check,basic_mrg,sale_mrg,card_mrg,point_mrg,app_rate,app_dc_rate,app_check,	`group`,order_term,	order_after_day,trd_stop_check,	reg_date,change_date,cd_user,order_sun,order_mon,order_tue,	order_wed,order_thu,order_fri,order_sat,bank_code,team_code,logst_mrg,miss_rate,logst_check,order_no_key,last_order_no,	logst_last_order_no,logst_check_no) values ('" + str(
        saup_code) + "','" + str(cst_code) + "','" + str(cst_name) + "','" + str(cst_no) + "','" + str(owner) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(tel) + "','" + str(checker_name) + "','" + str(checker_tel) + "','" + str(
        cst_check) + "','" + str(cst_type) + "','" + str(trd_start_date) + "','" + str(trd_end_date) + "','" + str(app_type) + "','" + str(
        app_date) + "','" + str(trd_check) + "','" + str(basic_mrg) + "','" + str(sale_mrg) + "','" + str(card_mrg) + "','" + str(
        point_mrg) + "','" + str(app_rate) + "','" + str(app_dc_rate) + "','" + str(app_check) + "','" + str(group) + "','" + str(
        order_term) + "','" + str(order_after_day) + "','" + str(trd_stop_check) + "','" + str(reg_date) + "','" + str(change_date) + "','" + str(
        cd_user) + "','" + str(order_sun) + "','" + str(order_mon) + "','" + str(order_tue) + "','" + str(order_wed) + "','" + str(
        order_thu) + "','" + str(order_fri) + "','" + str(order_sat) + "','" + str(bank_code) + "','" + str(team_code) + "','" + str(
        logst_mrg) + "','" + str(miss_rate) + "','" + str(logst_check) + "','" + str(order_no_key) + "','" + str(last_order_no) + "','" + str(
        logst_last_order_no) + "','" + str(logst_check_no) + "');"

    q.cursor17.execute(sql17)


f76 = open(r'C:\Users\youn\GRC\GRC_Geumchon.csv',encoding='utf-8-sig')
csvReader76 = csv.reader(f76)

for row in csvReader76:
    saup_code = (row[0])
    cst_code = (row[1])
    cst_name = (row[2])
    cst_no = (row[3])
    owner = (row[4])
    addr1 = (row[5])
    addr2 = (row[6])
    tel = (row[7])
    checker_name = (row[8])
    checker_tel = (row[9])
    cst_check = (row[10])
    cst_type = (row[11])
    trd_start_date = (row[12])
    trd_end_date = (row[13])
    app_type = (row[14])
    app_date = (row[15])
    trd_check = (row[16])
    basic_mrg = (row[17])
    sale_mrg = (row[18])
    card_mrg = (row[19])
    point_mrg = (row[20])
    app_rate = (row[21])
    app_dc_rate = (row[22])
    app_check = (row[23])
    group = (row[24])
    order_term = (row[25])
    order_after_day = (row[26])
    trd_stop_check = (row[27])
    reg_date = (row[28])
    change_date = (row[29])
    cd_user = (row[30])
    order_sun = (row[31])
    order_mon = (row[32])
    order_tue = (row[33])
    order_wed = (row[34])
    order_thu = (row[35])
    order_fri = (row[36])
    order_sat = (row[37])
    bank_code = (row[38])
    team_code = (row[39])
    logst_mrg = (row[40])
    miss_rate = (row[41])
    logst_check = (row[42])
    order_no_key = (row[43])
    last_order_no = (row[44])
    logst_last_order_no = (row[45])
    logst_check_no = (row[46])

    sql17 = "insert into m_grcmst (saup_code,cst_code,cst_name,	cst_no,	`owner`,`addr1`,`addr2`,`tel`,checker_name,checker_tel,cst_check,cst_type,trd_start_date,trd_end_date,app_type,app_date,trd_check,basic_mrg,sale_mrg,card_mrg,point_mrg,app_rate,app_dc_rate,app_check,	`group`,order_term,	order_after_day,trd_stop_check,	reg_date,change_date,cd_user,order_sun,order_mon,order_tue,	order_wed,order_thu,order_fri,order_sat,bank_code,team_code,logst_mrg,miss_rate,logst_check,order_no_key,last_order_no,	logst_last_order_no,logst_check_no) values ('" + str(
        saup_code) + "','" + str(cst_code) + "','" + str(cst_name) + "','" + str(cst_no) + "','" + str(owner) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(tel) + "','" + str(checker_name) + "','" + str(checker_tel) + "','" + str(
        cst_check) + "','" + str(cst_type) + "','" + str(trd_start_date) + "','" + str(trd_end_date) + "','" + str(app_type) + "','" + str(
        app_date) + "','" + str(trd_check) + "','" + str(basic_mrg) + "','" + str(sale_mrg) + "','" + str(card_mrg) + "','" + str(
        point_mrg) + "','" + str(app_rate) + "','" + str(app_dc_rate) + "','" + str(app_check) + "','" + str(group) + "','" + str(
        order_term) + "','" + str(order_after_day) + "','" + str(trd_stop_check) + "','" + str(reg_date) + "','" + str(change_date) + "','" + str(
        cd_user) + "','" + str(order_sun) + "','" + str(order_mon) + "','" + str(order_tue) + "','" + str(order_wed) + "','" + str(
        order_thu) + "','" + str(order_fri) + "','" + str(order_sat) + "','" + str(bank_code) + "','" + str(team_code) + "','" + str(
        logst_mrg) + "','" + str(miss_rate) + "','" + str(logst_check) + "','" + str(order_no_key) + "','" + str(last_order_no) + "','" + str(
        logst_last_order_no) + "','" + str(logst_check_no) + "');"

    q.cursor17.execute(sql17)


f77 = open(r'C:\Users\youn\GRC\GRC_Hwagok.csv',encoding='utf-8-sig')
csvReader77 = csv.reader(f77)

for row in csvReader77:
    saup_code = (row[0])
    cst_code = (row[1])
    cst_name = (row[2])
    cst_no = (row[3])
    owner = (row[4])
    addr1 = (row[5])
    addr2 = (row[6])
    tel = (row[7])
    checker_name = (row[8])
    checker_tel = (row[9])
    cst_check = (row[10])
    cst_type = (row[11])
    trd_start_date = (row[12])
    trd_end_date = (row[13])
    app_type = (row[14])
    app_date = (row[15])
    trd_check = (row[16])
    basic_mrg = (row[17])
    sale_mrg = (row[18])
    card_mrg = (row[19])
    point_mrg = (row[20])
    app_rate = (row[21])
    app_dc_rate = (row[22])
    app_check = (row[23])
    group = (row[24])
    order_term = (row[25])
    order_after_day = (row[26])
    trd_stop_check = (row[27])
    reg_date = (row[28])
    change_date = (row[29])
    cd_user = (row[30])
    order_sun = (row[31])
    order_mon = (row[32])
    order_tue = (row[33])
    order_wed = (row[34])
    order_thu = (row[35])
    order_fri = (row[36])
    order_sat = (row[37])
    bank_code = (row[38])
    team_code = (row[39])
    logst_mrg = (row[40])
    miss_rate = (row[41])
    logst_check = (row[42])
    order_no_key = (row[43])
    last_order_no = (row[44])
    logst_last_order_no = (row[45])
    logst_check_no = (row[46])

    sql17 = "insert into m_grcmst (saup_code,cst_code,cst_name,	cst_no,	`owner`,`addr1`,`addr2`,`tel`,checker_name,checker_tel,cst_check,cst_type,trd_start_date,trd_end_date,app_type,app_date,trd_check,basic_mrg,sale_mrg,card_mrg,point_mrg,app_rate,app_dc_rate,app_check,	`group`,order_term,	order_after_day,trd_stop_check,	reg_date,change_date,cd_user,order_sun,order_mon,order_tue,	order_wed,order_thu,order_fri,order_sat,bank_code,team_code,logst_mrg,miss_rate,logst_check,order_no_key,last_order_no,	logst_last_order_no,logst_check_no) values ('" + str(
        saup_code) + "','" + str(cst_code) + "','" + str(cst_name) + "','" + str(cst_no) + "','" + str(owner) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(tel) + "','" + str(checker_name) + "','" + str(checker_tel) + "','" + str(
        cst_check) + "','" + str(cst_type) + "','" + str(trd_start_date) + "','" + str(trd_end_date) + "','" + str(app_type) + "','" + str(
        app_date) + "','" + str(trd_check) + "','" + str(basic_mrg) + "','" + str(sale_mrg) + "','" + str(card_mrg) + "','" + str(
        point_mrg) + "','" + str(app_rate) + "','" + str(app_dc_rate) + "','" + str(app_check) + "','" + str(group) + "','" + str(
        order_term) + "','" + str(order_after_day) + "','" + str(trd_stop_check) + "','" + str(reg_date) + "','" + str(change_date) + "','" + str(
        cd_user) + "','" + str(order_sun) + "','" + str(order_mon) + "','" + str(order_tue) + "','" + str(order_wed) + "','" + str(
        order_thu) + "','" + str(order_fri) + "','" + str(order_sat) + "','" + str(bank_code) + "','" + str(team_code) + "','" + str(
        logst_mrg) + "','" + str(miss_rate) + "','" + str(logst_check) + "','" + str(order_no_key) + "','" + str(last_order_no) + "','" + str(
        logst_last_order_no) + "','" + str(logst_check_no) + "');"

    q.cursor17.execute(sql17)