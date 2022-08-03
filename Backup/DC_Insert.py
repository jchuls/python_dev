
import csv
import Query as q

# CSV 파일 경로
# f85 = open(r'C:\Users\youn\DC\DC_Cheonahn.csv',encoding='utf-8-sig')
# csvReader85 = csv.reader(f85)
#
# for row in csvReader85:
#     saup_code = (row[0])
#     barcode = (row[1])
#     member_check = (row[2])
#     dc_qty = (row[3])
#     dc_check = (row[4])
#     dc_price = (row[5])
#     pur_dc_price = (row[6])
#     limit_qty = (row[7])
#     dc_sale_qty = (row[8])
#     dc_start_date = (row[9])
#     dc_end_date = (row[10])
#     dc_attr = (row[11])
#     point_check = (row[12])
#     reg_date = (row[13])
#     change_date = (row[14])
#
#     sql18 = "insert into m_dcmst (saup_code,barcode,member_check,dc_qty,dc_check,dc_price,pur_dc_price,limit_qty,dc_sale_qty,dc_start_date,dc_end_date,dc_attr,point_check,reg_date,change_date) values ('" + str(saup_code) + "','" + str(
#         barcode) + "','" + str(member_check) + "','" + str(dc_qty) + "','" + str(dc_check) + "','" + str(dc_price) + "','" + str(pur_dc_price) + "','" + str(limit_qty) + "','" + str(dc_sale_qty) + "','" + str(
#         dc_start_date) + "','" + str(dc_end_date) + "','" + str(dc_attr) + "','" + str(point_check) + "','" + str(reg_date) + "','" + str(change_date) + "');"
#
#     q.cursor18.execute(sql18)


f86 = open(r'C:\Users\youn\DC\DC_Geumchon.csv',encoding='utf-8-sig')
csvReader86 = csv.reader(f86)

for row in csvReader86:
    saup_code = (row[0])
    barcode = (row[1])
    member_check = (row[2])
    dc_qty = (row[3])
    dc_check = (row[4])
    dc_price = (row[5])
    pur_dc_price = (row[6])
    limit_qty = (row[7])
    dc_sale_qty = (row[8])
    dc_start_date = (row[9])
    dc_end_date = (row[10])
    dc_attr = (row[11])
    point_check = (row[12])
    reg_date = (row[13])
    change_date = (row[14])

    sql18 = "insert into m_dcmst (saup_code,barcode,member_check,dc_qty,dc_check,dc_price,pur_dc_price,limit_qty,dc_sale_qty,dc_start_date,dc_end_date,dc_attr,point_check,reg_date,change_date) values ('" + str(saup_code) + "','" + str(
        barcode) + "','" + str(member_check) + "','" + str(dc_qty) + "','" + str(dc_check) + "','" + str(dc_price) + "','" + str(pur_dc_price) + "','" + str(limit_qty) + "','" + str(dc_sale_qty) + "','" + str(
        dc_start_date) + "','" + str(dc_end_date) + "','" + str(dc_attr) + "','" + str(point_check) + "','" + str(reg_date) + "','" + str(change_date) + "');"

    q.cursor18.execute(sql18)


# f87 = open(r'C:\Users\youn\DC\DC_Hwagok.csv',encoding='utf-8-sig')
# csvReader87 = csv.reader(f87)
#
# for row in csvReader87:
#     saup_code = (row[0])
#     barcode = (row[1])
#     member_check = (row[2])
#     dc_qty = (row[3])
#     dc_check = (row[4])
#     dc_price = (row[5])
#     pur_dc_price = (row[6])
#     limit_qty = (row[7])
#     dc_sale_qty = (row[8])
#     dc_start_date = (row[9])
#     dc_end_date = (row[10])
#     dc_attr = (row[11])
#     point_check = (row[12])
#     reg_date = (row[13])
#     change_date = (row[14])
#
#     sql18 = "insert into m_dcmst (saup_code,barcode,member_check,dc_qty,dc_check,dc_price,pur_dc_price,limit_qty,dc_sale_qty,dc_start_date,dc_end_date,dc_attr,point_check,reg_date,change_date) values ('" + str(saup_code) + "','" + str(
#         barcode) + "','" + str(member_check) + "','" + str(dc_qty) + "','" + str(dc_check) + "','" + str(dc_price) + "','" + str(pur_dc_price) + "','" + str(limit_qty) + "','" + str(dc_sale_qty) + "','" + str(
#         dc_start_date) + "','" + str(dc_end_date) + "','" + str(dc_attr) + "','" + str(point_check) + "','" + str(reg_date) + "','" + str(change_date) + "');"
#
#     q.cursor18.execute(sql18)