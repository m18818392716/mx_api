#-*- coding:utf-8 -*-
# @Time    : 2019/4/4 下午2:16
# @Author  : Susanna Chen
# @Site    : 
# @File    : operate_db_customer_userprofile.py
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

# 根据文件内容创建表头
# sql_1 = "CREATE TABLE customer_userprofile (code  VARCHAR(32),message  VARCHAR(100),data_lastLoginTime VARCHAR(100),data_id VARCHAR(100),data_baseCurrency VARCHAR(100),data_userName VARCHAR(100));"
#cur.execute(sql_1)#执行上述sql命令，首次运行时，需要执行上面的语句，用于创建table


# a = open("../jsonFiles/alldata.json", "r",encoding='UTF-8')
# out = a.read()

dict_headers = {"AMSESSION":"ukdata4", "Region":"uk", "Content-Type": r"application/json;charset=UTF-8"}
url = "https://proj.gtomato.com.cn/mobile/v1/customer/userprofile"
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

amsession = dict_headers['AMSESSION']
region = dict_headers['Region']

code = tmp['code']
message = tmp['message']

data_lastLoginTime = tmp['data']['lastLoginTime']
print(type(data_lastLoginTime))
data_id = tmp['data']['id']
data_baseCurrency = tmp['data']['baseCurrency']
data_userName = tmp['data']['userName']
E = [amsession, region, code, message, data_lastLoginTime, data_id, data_baseCurrency, data_userName]
print(E)
# x = len(data)
# print(x)
# i = 0

sql_2 = "insert into customer_userprofile(amsession, region, code, message, data_lastLoginTime, data_id, data_baseCurrency, data_userName) values (" + "'"+E[0]+"'" +","+ "'"+E[1]+"'" + ","+"'"+E[2]+"'" + ","+"'"+E[3]+"'" + ","+"'"+str(E[4])+"'" + ","+"'"+E[5]+"'" + ","+"'"+E[6]+"'" +","+"'"+E[7]+"'" +");"
# sql_2 = "insert into testDjango2.customer_userprofile(amsession, region, code, message, data_lastLoginTime, data_id, data_baseCurrency, data_userName) values ("+E[0]+","+E[1]+","+E[2]+","+E[3]+","+str(E[4])+","+E[5]+","+E[6]+","+E[7]+");"
print(sql_2)
# try:
#     cur.execute(sql_2)  # 执行上述sql命令
#     # 提交到数据库执行
#     print('提交到数据库执行ing...')
#     conn.commit()
# except:
#     # 如果发生错误则回滚
#     print('数据库rollback执行ing...')
#     conn.rollback()
# 关闭数据库连接
conn.close()