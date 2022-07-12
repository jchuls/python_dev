
import csv
import Query as q

# CSV 파일 경로
# f65 = open(r'C:\Users\youn\CJS\CJS_Cheonahn.csv',encoding='utf-8-sig')
# csvReader65 = csv.reader(f65)
#
# for row in csvReader65:
#     saup_code = (row[0])
#     sales_date = (row[1])
#     pos_no = (row[2])
#     rcp_no = (row[3])
#     member_no = (row[4])
#
#     sql16 = "insert into m_cjsmst (saup_code,sales_date,pos_no,	rcp_no,member_no) values ('" + str(
#         saup_code) + "','" + str(sales_date) + "','" + str(pos_no) + "','" + str(rcp_no) + "','" + str(member_no) + "');"
#
#     q.cursor16.execute(sql16)


# f66 = open(r'C:\Users\youn\CJS\CJS_Geumchon.csv',encoding='utf-8-sig')
# csvReader66 = csv.reader(f66)
#
# for row in csvReader66:
#     saup_code = (row[0])
#     sales_date = (row[1])
#     pos_no = (row[2])
#     rcp_no = (row[3])
#     member_no = (row[4])
#
#     sql16 = "insert into m_cjsmst (saup_code,sales_date,pos_no,	rcp_no,member_no) values ('" + str(
#         saup_code) + "','" + str(sales_date) + "','" + str(pos_no) + "','" + str(rcp_no) + "','" + str(member_no) + "');"
#
#     q.cursor16.execute(sql16)


f67 = open(r'C:\Users\youn\CJS\CJS_Hwagok.csv',encoding='utf-8-sig')
csvReader67 = csv.reader(f67)

for row in csvReader67:
    saup_code = (row[0])
    sales_date = (row[1])
    pos_no = (row[2])
    rcp_no = (row[3])
    member_no = (row[4])

    sql16 = "insert into m_cjsmst (saup_code,sales_date,pos_no,	rcp_no,member_no) values ('" + str(
        saup_code) + "','" + str(sales_date) + "','" + str(pos_no) + "','" + str(rcp_no) + "','" + str(member_no) + "');"

    q.cursor16.execute(sql16)
