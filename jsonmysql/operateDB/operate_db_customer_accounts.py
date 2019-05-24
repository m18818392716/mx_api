#-*- coding:utf-8 -*-
# @Time    : 2019/4/4 下午5:57
# @Author  : Susanna Chen
# @Site    : 
# @File    : operate_db_customer_accounts.py
# @Software: PyCharm

import json
import pymysql
import requests

conn = pymysql.connect(
    host='localhost',  # mysql服务器地址
    port=3306,  # 端口号
    user='root',  # 用户名
    passwd='',  # 密码
    db='',  # 数据库名称
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
url = "https://proj.gtomato.com.cn/mobile/v1/customer/5/accounts?currency=GBP&offset=0&limit=150"
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

data_accounts = tmp['data']['accounts']

data_accounts_id = tmp['data']['accounts']['id']
data_accounts_name = tmp['data']['accounts']['name']
data_accounts_weight = tmp['data']['accounts']['weight']
data_accounts_amount = tmp['data']['accounts']['amount']
data_accounts_externalId = tmp['data']['accounts']['externalId']
data_accounts_currency = tmp['data']['accounts']['currency']
data_accounts_baseCurrency = tmp['data']['accounts']['baseCurrency']

data_totalSize = tmp['data']['totalSize']


x = len(data_accounts)
print(data_accounts)
print(x)
i = 0
while i < x:
    M = tmp[i]

    H = [M['id'],M['name'],M['weight'],M['amount'],M['externalId'],M['currency'],M['baseCurrency']]
    print(H)
    sql_2 = "insert into jingweidu (customer_amsession,customer_token,code,message,data_accounts_id,data_accounts_name,data_accounts_weight,data_accounts_amount,data_accounts_externalId,data_accounts_currency,data_accounts_baseCurrency,data_totalSize) values (" + "'" + H[0] + "'" + "," + "'" + H[1] + "'" + "," + "'" + H[2] + "'" + "," + "'" + H[3] + "'" + "," + "'" + H[4] + "'" + "," + "'" + H[5] + "'" + ");"
    print(sql_2)
    print("============")
    i = i+1

