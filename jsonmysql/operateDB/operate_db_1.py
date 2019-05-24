#-*- coding:utf-8 -*-
# @Time    : 2019/4/4 下午12:49
# @Author  : Susanna Chen
# @Site    : 
# @File    : operate_db_1.py
# @Software: PyCharm

#python 3.6
# -*- coding:utf-8 -*-
__author__ = 'BH8ANK'

import json
import pymysql

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
sql_1 = "CREATE TABLE jingweidu (prov  VARCHAR(32),log  VARCHAR(100),lat VARCHAR(100),city VARCHAR(100),clog VARCHAR(100),clat VARCHAR(100));"
#cur.execute(sql_1)#执行上述sql命令，首次运行时，需要执行上面的语句，用于创建table

a = open("../jsonFiles/alldata.json", "r",encoding='UTF-8')
out = a.read()
print(type(out))
# tmp = json.dumps(out)
tmp = json.loads(out)
print(type(tmp))


x = len(tmp)
print(tmp)
print(x)
i = 0
while i < x:
    M = tmp[i]

    E = [M['name'],M['log'],M['lat']]
    print(E)
    j = len(M['children'])
    k = 0
    while k < j:
        F = [M['children'][k]['name'],M['children'][k]['log'],M['children'][k]['lat']]
        H = E + F
        print(H[0])
        sql_2 = "insert into jingweidu (prov,log,lat,city,clog,clat) values (" + "'"+H[0]+"'" +","+ "'"+H[1]+"'" + ","+"'"+H[2]+"'" + ","+"'"+H[3]+"'" + ","+"'"+H[4]+"'" + ","+"'"+H[5]+"'" + ");"
        print(sql_2)
        # cur.execute(sql_2)  # 执行上述sql命令
        k = k + 1
        # conn.commit()

    print("============")
    i = i+1

conn.close()