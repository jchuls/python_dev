
import csv
import Query as q
import test as ts



# CSV 파일 경로
# f12 = open(r'C:\Users\youn\Category\Category_Cheonahn.csv',encoding='utf-8-sig')
# csvReader12 = csv.reader(f12)
#
# for row in csvReader12:
#     saup_code = (row[0])
#     attr1 = (row[1])
#     attr2 = (row[2])
#     attr3 = (row[3])
#     attr_name = (row[4])
#     del_check = (row[5])
#     reg_date = (row[6])
#
#     moi_idx = ts.moi
#
#     sql11 = "insert into m_attmst_test (saup_code,moi_idx,attr1, attr2, attr3, attr_name, del_check, reg_date) values ('" + str(
#         saup_code) + "','" + str(moi_idx) + "', '" + str(attr1) + "', '" + str(attr2) + "', '" + str(attr3) + "', '" + str(
#         attr_name) + "', '" + str(del_check) + "', '" + str(reg_date) + "' );"
#
#     q.cursor1.execute(sql11)


f13 = open(r'C:\Users\youn\Category\Category_Geumchon.csv',encoding='utf-8-sig')
csvReader13 = csv.reader(f13)

for row in csvReader13:
    saup_code = (row[0])
    attr1 = (row[1])
    attr2 = (row[2])
    attr3 = (row[3])
    attr_name = (row[4])
    del_check = (row[5])
    reg_date = (row[6])

    moi_idx = ts.moi

    sql11 = "insert into m_attmst_test (saup_code,moi_idx,attr1, attr2, attr3, attr_name, del_check, reg_date) values ('" + str(
        saup_code) + "','" + str(moi_idx) + "', '" + str(attr1) + "', '" + str(attr2) + "', '" + str(attr3) + "', '" + str(
        attr_name) + "', '" + str(del_check) + "', '" + str(reg_date) + "' );"

    q.cursor1.execute(sql11)

f14 = open(r'C:\Users\youn\Category\Category_Hwagok.csv',encoding='utf-8-sig')
csvReader14 = csv.reader(f14)

for row in csvReader14:
    saup_code = (row[0])
    attr1 = (row[1])
    attr2 = (row[2])
    attr3 = (row[3])
    attr_name = (row[4])
    del_check = (row[5])
    reg_date = (row[6])

    moi_idx = ts.moi

    sql11 = "insert into m_attmst_test (saup_code,moi_idx,attr1, attr2, attr3, attr_name, del_check, reg_date) values ('" + str(
        saup_code) + "','" + str(moi_idx) + "', '" + str(attr1) + "', '" + str(attr2) + "', '" + str(attr3) + "', '" + str(
        attr_name) + "', '" + str(del_check) + "', '" + str(reg_date) + "' );"

    q.cursor1.execute(sql11)
