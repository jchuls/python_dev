
import csv
import Query as q
import re

# CSV 파일 경로
# f22 = open(r'C:\Users\youn\Member\Member_Cheonahn.csv',encoding='utf-8-sig')
# csvReader22 = csv.reader(f22)
#
# for row in csvReader22:
#     saup_code = (row[0])
#     member_code = (row[1])
#     member_name = (row[2])
#     birthday = (row[3])
#     member_grade = (row[4])
#     group = (row[5])
#     cp_name = (row[6])
#     owner = (row[7])
#     store_type = (row[8])
#     payday = (row[9])
#     zip_code = (row[10])
#     addr1 = (row[11])
#     addr2 = (row[12])
#     refund_cash = (row[13])
#     aprv_point_sum = (row[14])
#     use_point_sum = (row[15])
#     usable_point = (row[16])
#     amt_miss = (row[17])
#     join_date = (row[18])
#     sms_check = (row[19])
#     mail_check = (row[20])
#     status = (row[21])
#     last_day = (row[22])
#     change_date = (row[23])
#     cp_addr1 = (row[24])
#     cp_addr2 = (row[25])
#
#     sql12 = "insert into m_byrmst (saup_code,member_code,member_name, `birthday`, member_grade, `group`, cp_name, `owner`, store_type, payday, `zip_code`, `addr1`, `addr2`, refund_cash, aprv_point_sum, use_point_sum, usable_point, amt_miss, join_date, sms_check, mail_check, `status`, `last_day`, change_date,cp_addr1,cp_addr2) values ('" + str(
#         saup_code) + "','" + str(member_code) + "',	'" + str(member_name) + "',	'" + str(birthday) + "','" + str(member_grade) + "','" + str(group) + "','" + str(cp_name) + "','" + str(owner) + "','" + str(store_type) + "',	'" + str(payday) + "',	'" + re.sub('[\\\\]'," ",str(zip_code)) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(refund_cash) + "',	'" + str(
#         aprv_point_sum) + "',	'" + str(use_point_sum) + "','" + str(usable_point) + "','" + str(amt_miss) + "','" + str(join_date) + "','" + str(sms_check) + "','" + str(mail_check) + "','" + str(status) + "',	'" + str(last_day) + "','" + str(change_date) + "',	'" + str(cp_addr1) + "','" + str(cp_addr2) + "');"
#
#     q.cursor12.execute(sql12)


# f32 = open(r'C:\Users\youn\Member\Member_Geumchon.csv',encoding='utf-8-sig')
# csvReader32 = csv.reader(f32)
#
# for row in csvReader32:
#     saup_code = (row[0])
#     member_code = (row[1])
#     member_name = (row[2])
#     birthday = (row[3])
#     member_grade = (row[4])
#     group = (row[5])
#     cp_name = (row[6])
#     owner = (row[7])
#     store_type = (row[8])
#     payday = (row[9])
#     zip_code = (row[10])
#     addr1 = (row[11])
#     addr2 = (row[12])
#     refund_cash = (row[13])
#     aprv_point_sum = (row[14])
#     use_point_sum = (row[15])
#     usable_point = (row[16])
#     amt_miss = (row[17])
#     join_date = (row[18])
#     sms_check = (row[19])
#     mail_check = (row[20])
#     status = (row[21])
#     last_day = (row[22])
#     change_date = (row[23])
#     cp_addr1 = (row[24])
#     cp_addr2 = (row[25])
#
#     sql12 = "insert into m_byrmst (saup_code,member_code,member_name, `birthday`, member_grade, `group`, cp_name, `owner`, store_type, payday, `zip_code`, `addr1`, `addr2`, refund_cash, aprv_point_sum, use_point_sum, usable_point, amt_miss, join_date, sms_check, mail_check, `status`, `last_day`, change_date,cp_addr1,cp_addr2) values ('" + str(
#         saup_code) + "','" + str(member_code) + "',	'" + str(member_name) + "',	'" + str(birthday) + "','" + str(member_grade) + "','" + str(group) + "','" + str(cp_name) + "','" + str(owner) + "','" + str(store_type) + "',	'" + str(payday) + "',	'" + re.sub('[)(+\\\\]'," ",str(zip_code)) + "','" + re.sub('[\']'," ",str(addr1)) + "','" + str(addr2) + "','" + str(refund_cash) + "',	'" + str(
#         aprv_point_sum) + "',	'" + str(use_point_sum) + "','" + str(usable_point) + "','" + str(amt_miss) + "','" + str(join_date) + "','" + str(sms_check) + "','" + str(mail_check) + "','" + str(status) + "',	'" + str(last_day) + "','" + str(change_date) + "',	'" + str(cp_addr1) + "','" + str(cp_addr2) + "');"
#
#     q.cursor12.execute(sql12)


# f42 = open(r'C:\Users\youn\Member\Member_Hwagok.csv',encoding='utf-8-sig')
# csvReader42 = csv.reader(f42)
#
# for row in csvReader42:
#     saup_code = (row[0])
#     member_code = (row[1])
#     member_name = (row[2])
#     birthday = (row[3])
#     member_grade = (row[4])
#     group = (row[5])
#     cp_name = (row[6])
#     owner = (row[7])
#     store_type = (row[8])
#     payday = (row[9])
#     zip_code = (row[10])
#     addr1 = (row[11])
#     addr2 = (row[12])
#     refund_cash = (row[13])
#     aprv_point_sum = (row[14])
#     use_point_sum = (row[15])
#     usable_point = (row[16])
#     amt_miss = (row[17])
#     join_date = (row[18])
#     sms_check = (row[19])
#     mail_check = (row[20])
#     status = (row[21])
#     last_day = (row[22])
#     change_date = (row[23])
#     cp_addr1 = (row[24])
#     cp_addr2 = (row[25])
#
#     sql12 = "insert into m_byrmst (saup_code,member_code,member_name, `birthday`, member_grade, `group`, cp_name, `owner`, store_type, payday, `zip_code`, `addr1`, `addr2`, refund_cash, aprv_point_sum, use_point_sum, usable_point, amt_miss, join_date, sms_check, mail_check, `status`, `last_day`, change_date,cp_addr1,cp_addr2) values ('" + str(
#         saup_code) + "','" + str(member_code) + "',	'" + str(member_name) + "',	'" + str(birthday) + "','" + str(member_grade) + "','" + str(group) + "','" + str(cp_name) + "','" + str(owner) + "','" + str(store_type) + "',	'" + str(payday) + "',	'" + re.sub('[)(+\\\\]'," ",str(zip_code)) + "','" + str(addr1) + "','" + str(addr2) + "','" + str(refund_cash) + "',	'" + str(
#         aprv_point_sum) + "',	'" + str(use_point_sum) + "','" + str(usable_point) + "','" + str(amt_miss) + "','" + str(join_date) + "','" + str(sms_check) + "','" + str(mail_check) + "','" + str(status) + "',	'" + str(last_day) + "','" + str(change_date) + "',	'" + str(cp_addr1) + "','" + str(cp_addr2) + "');"
#
#     q.cursor12.execute(sql12)
