#-*- coding:utf-8 -*-
# @Time    : 2019/4/4 上午10:58
# @Author  : Susanna Chen
# @Site    : 
# @File    : operate_db.py
# @Software: PyCharm


import json
import pymysql


def get_data():
    with open('../jsonFiles/camera.json', 'r') as f:
        camera_text = json.load(f)  # 解析每一行数据
    return camera_text


def data_insert(camera_text):
    db = pymysql.connect("localhost", "root", "123456", "testDjango2")
    # db.clear('camera')
    cursor = db.cursor()
    # print(type(camera_text))
    value_ca = ((camera_text['camera']['created'], camera_text['camera']['type'],
                 camera_text['camera']['description'], camera_text['camera']['location']['locationID'],
                 camera_text['camera']['project_id'], camera_text['camera']['task_id'],
                 camera_text['camera']['camera_id'], camera_text['camera']['mu'],
                 camera_text['camera']['value']['x'], camera_text['camera']['value']['y'],
                 camera_text['camera']['ext_info']))

    value_lo = ((camera_text['camera']['location']['locationID'],
                 camera_text['camera']['location']['country'],
                 camera_text['camera']['location']['city'],
                 camera_text['camera']['location']['region']))
    # print(value_lo)
    # insert_lo = "insert into location(lidlocation,country,city,region) values (%s,%s,%s,%s)"
    insert_ca = "insert into camera(camera_created,camera_type,description,CIDlocation,IDproject,IDtask,IDcamera,mu,value_x,value_y,ext_info)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cursor = db.cursor()
    # cursor.execute(insert_lo,value_lo)
    cursor.execute(insert_ca, value_ca)
    db.commit()
    cursor.close()
    '''except Exception as e:
        db.rollback()
        print(str(e))
        break'''

if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    a=get_data()

    data_insert(a)