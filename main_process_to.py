import dbconfun as dbfun
import datetime as time

#기초 데이터 가공 처리 프로세스

#수집해야할 데이터 정보
#매출 테이블
one_data_table = 't_rawmst'
one_data_fild = ['moi_idx','concat(replace(sales_date,\'-\',\'\'),pos_no,rcp_no) as billcode','no_seq','(select t_itemmst.barcode from t_itemmst where t_itemmst.item_code = t_rawmst.barcode) as barcode','sale_qty','dc_price','tsales_amt','sales_date','member_no']

#회원코드 정보 테이블
one_mem_table = 't_cjsmst'

#가공된 데이터 저장 테이블
conv_table = 'm_sales_user'
conv_data_fild = ['moi_idx','billcode','no_seq','barcode','sale_qty','dc_price','sale_amt','sale_date','member_no']

succ_coll_mart = "select * from m_collection_log where mcl_msg = 'SUCC' and mcl_processing = '0' order by mcl_regDt ASC"
coll_data = dbfun.select(succ_coll_mart)

for mart_datainfo in coll_data:
    log_txts = ""
    now = time.datetime.now()
    log_txts = "\n"+mart_datainfo['mai_Company_num']+" 기초 데이터 가공시작 : " + str(now) + "\n"
    print(log_txts)

    fild_text = ', '.join(conv_data_fild)
    fild_text2 = ', '.join(one_data_fild)

    #판매데이터 가공수집
    data_select_insert_Query = "insert into " + conv_table + " ("+fild_text+") select "+fild_text2+" from " + one_data_table + " where data_end = '0' and moi_idx = '"+mart_datainfo['mai_Company_num']+"'"
    dbfun.merge(data_select_insert_Query)

    end_data_query = "update " + one_data_table + " set data_end='1' where data_end = 0 and moi_idx = '"+mart_datainfo['mai_Company_num']+"'"
    dbfun.select(end_data_query)

    #1차가공 완료시 1과 함께 업데이트
    upprocessing = "update m_collection_log set mcl_processing = '1' where mcl_msg = 'SUCC' and mai_Company_num = '"+mart_datainfo['mai_Company_num']+"'"
    dbfun.merge(upprocessing)
    
    #프로세싱 테이블에는 결과를 SUCC-LV1으로 한다.
    inprocessing = "insert into m_processing_log set mai_Company_num='"+str(mart_datainfo['mai_Company_num'])+"', mcl_idx='"+str(mart_datainfo['mcl_idx'])+"', mpl_msg='SUCC_MAIN_DATA', mpl_regDt=now()"
    dbfun.merge(inprocessing)

    now = time.datetime.now()
    log_txts = "\n"+mart_datainfo['mai_Company_num']+" 기초 데이터 가공완료 : " + str(now) + "\n"
    print(log_txts)