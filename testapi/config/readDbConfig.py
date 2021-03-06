# coding:utf-8

from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser

# ================读取db_config.ini文件设置=================


cur_path = os.path.dirname(os.path.realpath(__file__))
configPath = os.path.join(cur_path, "db_config.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ================封装MySQL基本操作=================
class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(
                host=host,
                user=user,
                password=password,
                db=db,
                charset="utf8mb4",
                cursorclass=cursors.DictCursor
            )
        except OperationalError as e:
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self, tabel_name):
        real_sql = "delete from " + tabel_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ",".join(table_data.values())

        # real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES ('%s')" % value
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES  (" + value + ")" + ";"

        # real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES('%s') %(" + value + ")" + ";"
        # real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES ('%s')" % + "(" + value + ")" + ";"

        # sql = "INSERT INTO table(key) VALUES ('%s')" % (value)
        # print(sql)
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    # 关闭数据库连接
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    table_name = "testapi_sign_event"
    data = {"user_id": 12,
            "name": "红米",
            # "amount": 2000,
            # "status": 1,
            "address": "北京会展中心",
            "start_time": "2018-10-30 08:00:00",
            }
    db.clear(table_name)
    db.insert(table_name, data)
    db.close()