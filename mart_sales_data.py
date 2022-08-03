#자동아닌 별도로 작동하는 프로세스
import dbconfun as dbfun
import datetime as time

from array import array

log_txts = ""
now = time.datetime.now()
log_txts = "\n작동시간 : " + str(now) + "\n"

#---------------테이블 정의---------------
#마트 판매 데이터 정보 테이블
one_sales_table = "m_sales_user"

#월별 마트 매출 테이블
month_sales_table = "m_pay_month_sales"

#일별 마트 매출 테이블
day_sales_table = "m_pay_day_sales"

#월별 객수 테이블
month_user_table = "m_pay_month_user"

#일별 객수 테이블
day_user_table = "m_pay_day_user"

#할인정보
day_sale_table = "m_pay_month_sale"
#---------------테이블 정의---------------

martidx = "2206213"

#월별 매출 데이터
salse_Query = "SELECT moi_idx,DATE_FORMAT(sales_date,\"%Y-%m\") AS sales_date, SUM(sale_amt) AS sale_amt, SUM(dc_price) as sale FROM " + one_sales_table + " where data_end = 0 and moi_idx = '"+martidx+"' GROUP BY moi_idx,DATE_FORMAT(sales_date,\"%Y-%m\")"

mart_info_data = dbfun.select(salse_Query)

for mdata in mart_info_data:
    #판매 일자 분할 처리 요일 or 월별 매출 데이터 산출을 위해
    dayexplode = str(mdata['sales_date']).split("-")
    
    data_space_check = "select count(*) as cnts from " + month_sales_table + " where mai_Company_num = '"+mdata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"';"
    data_space_result = dbfun.select(data_space_check)
        
    if(data_space_result[0]['cnts'] == 0):
        data_space_insert = "insert into " + month_sales_table + " set mai_Company_num = '"+mdata['moi_idx']+"', mms_year = '"+dayexplode[0]+"', mms_"+dayexplode[1]+"m = '"+str(mdata['sale_amt'])+"';"
    else:
        data_space_insert = "update " + month_sales_table + " set mms_"+dayexplode[1]+"m = '"+str(mdata['sale_amt'])+"' where mai_Company_num = '"+mdata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"';"
    dbfun.select(data_space_insert)

    #할인된 금액 데이터 
    data_space_check = "select count(*) as cnts from " + day_sale_table + " where mai_Company_num = '"+mdata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"';"
    data_space_result = dbfun.select(data_space_check)
        
    if(data_space_result[0]['cnts'] == 0):
        data_space_insert = "insert into " + day_sale_table + " set mai_Company_num = '"+mdata['moi_idx']+"', mms_year = '"+dayexplode[0]+"', mms_"+dayexplode[1]+"m = '"+str(mdata['sale'])+"';"
    else:
        data_space_insert = "update " + day_sale_table + " set mms_"+dayexplode[1]+"m = '"+str(mdata['sale'])+"' where mai_Company_num = '"+mdata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"';"
    dbfun.select(data_space_insert)

    end_data_query = "update " + one_sales_table + " set data_end='1' where DATE_FORMAT(sales_date,\"%Y-%m\") = '" + mdata['sales_date'] + "' and data_end = 0 and moi_idx = '"+martidx+"'"
    dbfun.select(end_data_query)
log_txts += "월별 매출 데이터, 월별 할인금액 가공완료 : " + str(now) + "\n"
#일자별 매출 데이터
salse_day_Query = "SELECT moi_idx,DATE_FORMAT(sales_date,\"%Y-%m-%d\") AS sales_date, SUM(sale_amt) AS sale_amt FROM " + one_sales_table + " where data_end = 1 and moi_idx = '"+martidx+"' GROUP BY moi_idx,DATE_FORMAT(sales_date,\"%Y-%m-%d\")"

mart_info_day_data = dbfun.select(salse_day_Query)

for ddata in mart_info_day_data:
    #판매 일자 분할 처리 요일 or 월별 매출 데이터 산출을 위해
    dayexplode = str(ddata['sales_date']).split("-")
    
    data_space_check = "select count(*) as cnts from " + day_sales_table + " where mai_Company_num = '"+ddata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"' and mss_month = '" + dayexplode[1] + "';"
    data_space_result = dbfun.select(data_space_check)
        
    if(data_space_result[0]['cnts'] == 0):
        data_space_insert = "insert into " + day_sales_table + " set mai_Company_num = '"+ddata['moi_idx']+"', mms_year = '"+dayexplode[0]+"', mss_month = '"+dayexplode[1]+"', mms_"+dayexplode[2]+"d = '"+str(ddata['sale_amt'])+"';"
    else:
        data_space_insert = "update " + day_sales_table + " set mms_"+dayexplode[2]+"d = '"+str(ddata['sale_amt'])+"' where mai_Company_num = '"+ddata['moi_idx']+"' and mms_year = '"+dayexplode[0]+"' and mss_month = '" + dayexplode[1] + "';"
    dbfun.select(data_space_insert)


end_data_query = "update " + one_sales_table + " set data_end='2' where data_end = '1' and moi_idx = '"+martidx+"'"
dbfun.select(end_data_query)
log_txts += "일별 매출 데이터 가공완료 : " + str(now) + "\n"
#사용할 일자별 변수 생성
use_day_Query = "SELECT sales_date FROM m_rawmst where moi_idx='"+martidx+"' and data_end='2' GROUP BY sales_date"
use_day_data = dbfun.select(use_day_Query)
mon_userdata = {}
day_userdata = {}
for usedata in use_day_data:
    day_userdata[usedata['sales_date']] = 0
    dayexplode = str(usedata['sales_date']).split("-")
    mon_userdata[dayexplode[0] + "-" +dayexplode[1]] = 0

#일자별 객수 추출
user_day_Query = "SELECT sales_date,moi_idx,COUNT(*) AS cnt FROM " + one_sales_table + " WHERE data_end = 2 and moi_idx = '"+martidx+"' GROUP BY moi_idx,CONCAT(REPLACE(sales_date,'-',''),pos_no,rcp_no)"
user_info_day_data = dbfun.select(user_day_Query)
for uddata in user_info_day_data:
    dayexplode = str(uddata['sales_date']).split("-")
    mon_userdata[dayexplode[0] + "-" +dayexplode[1]] += 1
    day_userdata[uddata['sales_date']] += 1

#만들어진 객수 정보 입력 처리
for usedata in use_day_data:
    dayexplode = str(usedata['sales_date']).split("-")
    data_space_check = "select count(*) as cnts from " + month_user_table + " where mai_Company_num = '"+martidx+"' and mms_year = '"+dayexplode[0]+"';"
    data_space_result = dbfun.select(data_space_check)
    
    if(data_space_result[0]['cnts'] == 0):
        data_space_insert = "insert into " + month_user_table + " set mai_Company_num = '"+martidx+"', mms_year = '"+dayexplode[0]+"', mms_"+dayexplode[1]+"m = '"+str(mon_userdata[dayexplode[0] + "-" +dayexplode[1]])+"';"
    else:
        data_space_insert = "update " + month_user_table + " set mms_"+dayexplode[1]+"m = '"+str(mon_userdata[dayexplode[0] + "-" +dayexplode[1]])+"' where mai_Company_num = '"+martidx+"' and mms_year = '"+dayexplode[0]+"';"
    dbfun.select(data_space_insert)

    data_space_check = "select count(*) as cnts from " + day_user_table + " where mai_Company_num = '"+martidx+"' and mms_year = '"+dayexplode[0]+"' and mss_month = '" + dayexplode[1] + "';"
    data_space_result = dbfun.select(data_space_check)

    if(data_space_result[0]['cnts'] == 0):
        data_space_insert = "insert into " + day_user_table + " set mai_Company_num = '"+martidx+"', mms_year = '"+dayexplode[0]+"', mss_month = '"+dayexplode[1]+"', mms_"+dayexplode[2]+"d = '"+str(day_userdata[usedata['sales_date']])+"';"
    else:
        data_space_insert = "update " + day_user_table + " set mms_"+dayexplode[2]+"d = '"+str(day_userdata[usedata['sales_date']])+"' where mai_Company_num = '"+martidx+"' and mms_year = '"+dayexplode[0]+"' and mss_month = '" + dayexplode[1] + "';"
    dbfun.select(data_space_insert)
    
end_data_query = "update " + one_sales_table + " set data_end='3' where data_end = '2' and moi_idx = '"+martidx+"'"
dbfun.select(end_data_query)

salse_day_Query = "SELECT moi_idx,DATE_FORMAT(sales_date,\"%Y-%m-%d\") AS sales_date, SUM(sale_amt) AS sale_amt FROM " + one_sales_table + " where data_end = 3 and moi_idx = '"+martidx+"' GROUP BY moi_idx,DATE_FORMAT(sales_date,\"%Y-%m-%d\")"

mart_info_day_data = dbfun.select(salse_day_Query)

log_txts += "월,일 객수데이터 가공완료 : " + str(now) + "\n"
log_txts += "초기 정보 데이터 가공완료 : " + str(now) + "\n"
now = time.datetime.now()
log_txts += "종료시간 : " + str(now) + "\n"

print(log_txts)