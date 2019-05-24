#-*- coding:utf-8 -*-
# @Time    : 2019/4/4 下午3:35
# @Author  : Susanna Chen
# @Site    : 
# @File    : operate_db_customer_overview.py
# @Software: PyCharm

import json
import pymysql
import requests

conn = pymysql.connect(
    host='localhost',  # mysql服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='123456789',  # 密码
    db='testDjango2',  # 数据库名称
    charset='utf8',  # 连接编码，根据需要填写
)
cur = conn.cursor()  # 创建并返回游标
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("Database version : %s " % data) # 结果表明已经连接成功

# 根据文件内容创建表头
# sql_1 = "CREATE TABLE customer_userprofile (code  VARCHAR(32),message  VARCHAR(100),data_lastLoginTime VARCHAR(100),data_id VARCHAR(100),data_baseCurrency VARCHAR(100),data_userName VARCHAR(100));"
#cur.execute(sql_1)#执行上述sql命令，首次运行时，需要执行上面的语句，用于创建table


# a = open("../jsonFiles/alldata.json", "r",encoding='UTF-8')
# out = a.read()

dict_headers = {"AMSESSION":"ukdata0", "LtpaToken2":"LtpaToken2_0_UK", "Content-Type": r"application/json;charset=UTF-8"}
url = "https://proj.gtomato.com.cn/mobile/v1/customer/0/overview?currency=GBP"
response = requests.get(url, headers=dict_headers)
# print(type(response.json()))
# print(type(json.dumps(response.json())))
# print(response.json())
# print(json.dumps(response.json()))
json_str = json.dumps(response.json())

# tmp = json.dumps(out)

tmp = json.loads(json_str)
print(type(tmp))
print(tmp)

customer_amsession = dict_headers['AMSESSION']
customer_token = dict_headers['LtpaToken2']

code = tmp['code']
message = tmp['message']

data_customer_name = tmp['data']['customer']['name']
data_customer_amount = tmp['data']['customer']['amount']
data_customer_currency = tmp['data']['customer']['currency']
data_customer_bookingCenter = tmp['data']['customer']['bookingCenter']
data_customer_updateDate = tmp['data']['customer']['updateDate']
print(type(data_customer_updateDate))
data_customer_liabilitiesAmount = tmp['data']['customer']['liabilitiesAmount']
data_customer_liabilitiesCurrency = tmp['data']['customer']['liabilitiesCurrency']
data_customer_netAssetsAmount = tmp['data']['customer']['netAssetsAmount']
data_customer_netAssetsCurrency = tmp['data']['customer']['netAssetsCurrency']

data_ytd_amount = tmp['data']['ytd']['amount']
data_ytd_currency = tmp['data']['ytd']['currency']

data_hasLiabilities = tmp['data']['hasLiabilities']
print(type(data_hasLiabilities))
data_newDocumentCount = tmp['data']['newDocumentCount']
print(type(data_newDocumentCount))

E = [customer_amsession, customer_token, code, message, data_customer_name, data_customer_amount, data_customer_currency, data_customer_bookingCenter, data_customer_updateDate, data_customer_liabilitiesAmount, data_customer_liabilitiesCurrency, data_customer_netAssetsAmount, data_customer_netAssetsCurrency, data_ytd_amount, data_ytd_currency, data_hasLiabilities, data_newDocumentCount]
print(E)
# x = len(data)
# print(x)
# i = 0

# sql_2 = "insert into customer_overview (customer_amsession, customer_token, code, message, data_customer_name, data_customer_amount, data_customer_currency, data_customer_bookingCenter, data_customer_updateDate, data_customer_liabilitiesAmount, data_customer_liabilitiesCurrency, data_customer_netAssetsAmount, data_customer_netAssetsCurrency, data_ytd_amount, data_ytd_currency, data_hasLiabilities, data_newDocumentCount) values (" + "'"+E[0]+"'" +","+ "'"+E[1]+"'" + ","+"'"+E[2]+"'" + ","+"'"+E[3]+"'" + ","+"'"+str(E[4])+"'" + ","+"'"+str(E[5])+"'" + ","+"'"+E[6]+"'" +","+"'"+E[7]+"'" +","+"'"+E[8]+"'" +","+"'"+E[9]+"'" +","+"'"+E[10]+"'" +","+"'"+E[11]+"'" +","+"'"+E[12]+"'" +","+"'"+E[13]+"'" +","+"'"+E[14]+"'" +","+"'"+E[15]+"'" +","+ E[16] +");"
# print(sql_2)
# sql_2 = "insert into test_db (id,username,age) values ('%s','%s','%s'，'%s','%s','%s'，'%s','%s','%s'，'%s','%s','%s'，'%s','%s','%s'，'%s','%s','%s')" % (1,'kerk',25)
sql_2 = "insert into customer_overview (customer_amsession, customer_token, code, message, data_customer_name, data_customer_amount, data_customer_currency, data_customer_bookingCenter, data_customer_updateDate, data_customer_liabilitiesAmount, data_customer_liabilitiesCurrency, data_customer_netAssetsAmount, data_customer_netAssetsCurrency, data_ytd_amount, data_ytd_currency, data_hasLiabilities, data_newDocumentCount) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%s,'%s');" % (E[0], E[1], E[2], E[3], E[4], E[5], E[6], E[7], E[8], E[9], E[10], E[11], E[12], E[13], E[14], E[15], E[16])
print(sql_2)

try:
    cur.execute(sql_2)  # 执行上述sql命令
    # 提交到数据库执行
    print('提交到数据库执行ing...')
    conn.commit()
except Exception as e:
    # 如果发生错误则回滚
    print('数据库rollback执行ing...')
    conn.rollback()
    print(str(e))

# 关闭数据库连接
conn.close()

# H=[1,'susanna','123456']