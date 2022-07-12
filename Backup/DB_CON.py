import json
import DB_in
from _collections import OrderedDict
import pymysql

data = DB_in



#DB 연결
#TSERVER = {'host':'192.168.10.83', 'user':'root', 'password':'data!@34', 'database':'mommart', 'charset':'utf8', 'port':3306}, #TEST SERVER
#HWAGOK = {'host':'118.37.31.111', 'user':'momma', 'password':'akaakajrwk12#$', 'database':'hysvrdb', 'charset':'euckr', 'port':13306}, #화곡점
#GEUMCHON = {'host':'116.44.173.151', 'user':'momma', 'password':'momma123', 'database':'hysvrdb', 'charset':'euckr', 'port':13306}, #금촌점
#CHEONAHN = {'host':'61.97.37.50', 'user':'momma', 'password':'1234qwer', 'database':'hysvrdb', 'charset':'utf8', 'port':13306} #천안점

#print(json.dumps(CHEONAHN,ensure_ascii=False,indent="\t"))

#with open('TEST.json','w',encoding='utf-8') as make_file:
#        json.dump(CHEONAHN,make_file,ensure_ascii=False,indent="\t")

# [Return] = json.load([File Descriptor])
#with open('TEST.json', 'r', encoding='utf-8') as file_load:
#        data = json.load(file_load, object_pairs_hook=OrderedDict)

#FILE_NAME = "TEST.json"

#def main():
        # Ready for data
#         server_group = OrderedDict()
#         server_info = OrderedDict()


#        with open(FILE_NAME, "w", encoding="utf-8") as f:
#        json.dump(server_group, f, ensure_ascii=False, indent="\t")
#        try:
#            with open('TEST.json', 'w', encoding='utf-8') as make_file:
#                json.dump(TSERVER, make_file, ensure_ascii=False, indent="\t")
#        except:
#            print("ERROR")
#        print(data)
#if __name__ == "__main__":
#    main()