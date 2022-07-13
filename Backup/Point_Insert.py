
import csv
import Query as q

# CSV 파일 경로
# f55 = open(r'C:\Users\youn\Point\Point_Cheonahn.csv',encoding='utf-8-sig')
# csvReader55 = csv.reader(f55)
#
# for row in csvReader55:
#     saup_code = (row[0])
#     member_no = (row[1])
#     aprv_point = (row[2])
#     use_point = (row[3])
#     adj_point = (row[4])
#     adj_check = (row[5])
#     reg_date = (row[6])
#     sale_date = (row[7])
#     sale_pos = (row[8])
#     sale_pos_no = (row[9])
#
#     sql15 = "insert into m_ptmst (saup_code,member_no,aprv_point,use_point,adj_point,adj_check,reg_date,sale_date,`sale_pos`,sale_pos_no) values ('" + str(
#         saup_code) + "','" + str(member_no) + "','" + str(aprv_point) + "','" + str(use_point) + "','" + str(
#         adj_point) + "','" + str(adj_check) + "','" + str(
#         reg_date) + "','" + str(sale_date) + "','" + str(sale_pos) + "','" + str(sale_pos_no) + "');"
#
#     q.cursor15.execute(sql15)


f56 = open(r'C:\Users\youn\Point\Point_Geumchon.csv',encoding='utf-8-sig')
csvReader56 = csv.reader(f56)

for row in csvReader56:
    saup_code = (row[0])
    member_no = (row[1])
    aprv_point = (row[2])
    use_point = (row[3])
    adj_point = (row[4])
    adj_check = (row[5])
    reg_date = (row[6])
    sale_date = (row[7])
    sale_pos = (row[8])
    sale_pos_no = (row[9])

    sql15 = "insert into m_ptmst (saup_code,member_no,aprv_point,use_point,adj_point,adj_check,reg_date,sale_date,`sale_pos`,sale_pos_no) values ('" + str(
        saup_code) + "','" + str(member_no) + "','" + str(aprv_point) + "','" + str(use_point) + "','" + str(
        adj_point) + "','" + str(adj_check) + "','" + str(
        reg_date) + "','" + str(sale_date) + "','" + str(sale_pos) + "','" + str(sale_pos_no) + "');"

    q.cursor15.execute(sql15)


# f57 = open(r'C:\Users\youn\Point\Point_Hwagok.csv',encoding='utf-8-sig')
# csvReader57 = csv.reader(f57)
#
# for row in csvReader57:
#     saup_code = (row[0])
#     member_no = (row[1])
#     aprv_point = (row[2])
#     use_point = (row[3])
#     adj_point = (row[4])
#     adj_check = (row[5])
#     reg_date = (row[6])
#     sale_date = (row[7])
#     sale_pos = (row[8])
#     sale_pos_no = (row[9])
#
#     sql15 = "insert into m_ptmst (saup_code,member_no,aprv_point,use_point,adj_point,adj_check,reg_date,sale_date,`sale_pos`,sale_pos_no) values ('" + str(
#         saup_code) + "','" + str(member_no) + "','" + str(aprv_point) + "','" + str(use_point) + "','" + str(
#         adj_point) + "','" + str(adj_check) + "','" + str(
#         reg_date) + "','" + str(sale_date) + "','" + str(sale_pos) + "','" + str(sale_pos_no) + "');"
#
#     q.cursor15.execute(sql15)
