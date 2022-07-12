
import json
import pymysql

path = "./DB_in.json"

data = {}
data['TEST'] = []
data['Cheonahn'] = []
data['Geumchon'] = []
data['Hwagok'] = []

#TEST SERVER
data['TEST'].append({
      "host": "192.168.10.83",
      "user": "root",
      "password": "data!@34",
      "database": "mommart",
      "charset": "utf8",
      "port": 3306
})

#화곡점
data['Hwagok'].append({
      "host": "118.37.31.111",
      "user": "momma",
      "password": "akaakajrwk12#$",
      "database": "hysvrdb",
      "charset": "utf8",
      "port": 13306
 })

#금촌점
data['Geumchon'].append({
      "host": "116.44.173.151",
      "user": "momma",
      "password": "momma123",
      "database": "hysvrdb",
      "charset": "utf8",
      "port": 13306
 })

#천안점
data['Cheonahn'].append({
      "host": "61.97.37.50",
      "user": "momma",
      "password": "1234qwer",
      "database": "hysvrdb",
      "charset": "utf8",
      "port": 13306
 })

with open(path,'w') as outf:
      json.dump(data,outf,indent=4)

with open(path,'r') as json_f:
      json_data=json.load(json_f)

conn1=data["TEST"][0]
conn2=data["Cheonahn"][0]
conn3=data["Geumchon"][0]
conn4=data["Hwagok"][0]

dbc1 = pymysql.connect(host=conn1['host'],user=conn1['user'],password=conn1['password'],database=conn1['database'],charset=conn1['charset'],port=conn1['port'])
dbc2 = pymysql.connect(host=conn2['host'],user=conn2['user'],password=conn2['password'],database=conn2['database'],charset=conn2['charset'],port=conn2['port'])
dbc3 = pymysql.connect(host=conn3['host'],user=conn3['user'],password=conn3['password'],database=conn3['database'],charset=conn3['charset'],port=conn3['port'])
dbc4 = pymysql.connect(host=conn4['host'],user=conn4['user'],password=conn4['password'],database=conn4['database'],charset=conn4['charset'],port=conn4['port'])
