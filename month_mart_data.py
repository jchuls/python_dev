import dbconfun as dbfun
import datetime as time

from array import array

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

mem_pay_table = "m_month_mem_pay"
#---------------테이블 정의---------------

succ_coll_mart = "select * from m_processing_log where mpl_msg = 'SUCC_MAIN_DATA' and mpl_processing = '0' order by mpl_regDt ASC"
coll_data = dbfun.select(succ_coll_mart)

for mart_datainfo in coll_data:
    log_txts = ""
    now = time.datetime.now()
    log_txts = "\n작동시간 : " + str(now) + "\n"

    martidx = mart_datainfo['mai_Company_num']

    #월별 매출 데이터
    salse_Query = "SELECT moi_idx,DATE_FORMAT(sale_date,\"%Y-%m\") AS sales_date, SUM(sale_amt) AS sale_amt, SUM(dc_price) as sale FROM " + one_sales_table + " where data_end = 0 and moi_idx = '"+martidx+"' GROUP BY moi_idx,DATE_FORMAT(sale_date,\"%Y-%m\")"

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

        end_data_query = "update " + one_sales_table + " set data_end='1' where DATE_FORMAT(sale_date,\"%Y-%m\") = '" + mdata['sales_date'] + "' and data_end = 0 and moi_idx = '"+martidx+"'"
        dbfun.select(end_data_query)
    now = time.datetime.now()
    log_txts += "월별 매출 데이터, 월별 할인금액 가공완료 : " + str(now) + "\n"

    #일자별 매출 데이터
    salse_day_Query = "SELECT moi_idx,DATE_FORMAT(sale_date,\"%Y-%m-%d\") AS sales_date, SUM(sale_amt) AS sale_amt FROM " + one_sales_table + " where data_end = 1 and moi_idx = '"+martidx+"' GROUP BY moi_idx,DATE_FORMAT(sale_date,\"%Y-%m-%d\")"

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
    now = time.datetime.now()
    log_txts += "일별 매출 데이터 가공완료 : " + str(now) + "\n"

    #사용할 일자별 변수 생성
    use_day_Query = "SELECT DATE_FORMAT(sale_date,\"%Y-%m-%d\") AS sales_date FROM " + one_sales_table + " where moi_idx='"+martidx+"' and data_end='2' GROUP BY DATE_FORMAT(sale_date,\"%Y-%m-%d\")"
    use_day_data = dbfun.select(use_day_Query)
    mon_userdata = {}
    day_userdata = {}
    for usedata in use_day_data:
        day_userdata[usedata['sales_date']] = 0
        dayexplode = str(usedata['sales_date']).split("-")
        mon_userdata[dayexplode[0] + "-" +dayexplode[1]] = 0

    #일자별 객수 추출
    user_day_Query = "SELECT DATE_FORMAT(sale_date,\"%Y-%m-%d\") AS sales_date,moi_idx,COUNT(*) AS cnt FROM " + one_sales_table + " WHERE data_end = 2 and moi_idx = '"+martidx+"' GROUP BY moi_idx,billcode"
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

    now = time.datetime.now()
    log_txts += "월,일 객수 데이터 가공완료 : " + str(now) + "\n"

    salse_user_Query = "SELECT moi_idx,if(member_no = 0,0,1) as memno,DATE_FORMAT(sale_date,\"%Y-%m\") AS sales_date, SUM(sale_amt) AS sale_amt FROM " + one_sales_table + " where data_end = 3 and moi_idx = '"+martidx+"' GROUP BY moi_idx,if(member_no = 0,0,1),DATE_FORMAT(sale_date,\"%Y-%m\")"

    mart_info_day_data = dbfun.select(salse_user_Query)
    mempay = {}
    nonepay = {}
    for userdata in mart_info_day_data:
        dayexplode = str(userdata['sales_date']).split("-")

        data_space_check = "select count(*) as cnts from " + mem_pay_table + " where mai_Company_num = '"+martidx+"' and mms_year = '"+dayexplode[0]+"' and mms_type = '"+str(userdata['memno'])+"';"
        data_space_result = dbfun.select(data_space_check)
    
        if(data_space_result[0]['cnts'] == 0):
            data_space_insert = "insert into " + mem_pay_table + " set mai_Company_num = '"+martidx+"', mms_year = '"+str(dayexplode[0])+"', mms_type = '"+str(userdata['memno'])+"', mms_"+str(dayexplode[1])+"m = '"+str(userdata['sale_amt'])+"';"
        else:
            data_space_insert = "update " + mem_pay_table + " set mms_"+str(dayexplode[1])+"m = '"+str(userdata['sale_amt'])+"' where mai_Company_num = '"+str(martidx)+"' and mms_year = '"+str(dayexplode[0])+"' and mms_type = '"+str(userdata['memno'])+"';"

        dbfun.select(data_space_insert)

    now = time.datetime.now()
    log_txts += "회원,비회원 매출 월별 데이터 가공완료 : " + str(now) + "\n"
    
    end_data_query = "update " + one_sales_table + " set data_end='4' where data_end = '3' and moi_idx = '"+martidx+"'"
    dbfun.select(end_data_query)
        
        
    #1차가공 완료시 1과 함께 업데이트
    upprocessing = "update m_processing_log set mpl_processing = '1' where mpl_msg = 'SUCC_MAIN_DATA' and mpl_idx = '"+str(mart_datainfo['mpl_idx'])+"'"
    dbfun.merge(upprocessing)
    
    #프로세싱 테이블에는 결과를 SUCC-LV2으로 한다.
    inprocessing = "insert into m_processing_log set mai_Company_num='"+str(mart_datainfo['mai_Company_num'])+"', mcl_idx='"+str(mart_datainfo['mpl_idx'])+"', mpl_msg='SUCC_LV2_DATA', mpl_regDt=now()"
    dbfun.merge(inprocessing)
    now = time.datetime.now()
    log_txts += "월,일 객수데이터 가공완료 : " + str(now) + "\n"
    now = time.datetime.now()
    log_txts += "종료시간 : " + str(now) + "\n"

    print(log_txts)