#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午2:29
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo.py
# @Software: PyCharm

import json
from collections import OrderedDict

class A():
    def __init__(self):
        self.name="xx"
        self.age=30
a=A()
print(json.dumps(a.__dict__))


class Student(object):
    def __init__(self, name, age, score, reward):
        self.name = name
        self.age = age
        self.score = score
        self.reward = reward


def dict2student(d):
    return Student(d['name'], d['age'], d['score'], d['reward'])


json_str = '{"name": "Bob", "age": 20, "score": 88, "reward": ["三好学生", "优秀团干", "最佳辩手"]}'
student = json.loads(json_str, object_hook=dict2student)
print(type(student))
print(student.name)




class CustomerUserProfileResponse(object):
    # age = 10
    def __init__(self, code, message, data):
    # def __init__(self, data):

        self.code = code
        self.message = message
        self.data = data
        print("调用父类构造函数")

    # def getAge(self):
    #     if CustomerUserProfileResponse.age < 1:
    #         return 1
    #     else:
    #         return CustomerUserProfileResponse.age
    #
    # def setAge(self, value):
    #     if value > 2: value = 2
    #     self.age = value

    def setCode(self,code):
        self.code = code

    def getCode(self):
        return self.code

    def setMessage(self, message):
        self.message = message

    def getMessage(self):
        return self.message

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data


def dict2CustomerUserProfileResponse(d):
    return CustomerUserProfileResponse(d['code'], d['message'], d['data'])
    # return CustomerUserProfileResponse(d['data'])


json_str1 = '{"code": "0", "message": "success", "data": {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"}}'
# json_str1 = '{"data": {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"}}'
# json_str1 = '{"code": "0", "message": "success"}'
print('json_str1的数据类型为：%s' % type(json_str1))
customerUserProfileResponse = json.loads(json_str1, object_pairs_hook=OrderedDict)
# customerUserProfileResponse = json.loads(json_str1, object_hook=dict2CustomerUserProfileResponse)
print('customerUserProfileResponse的数据类型为：%s' % type(customerUserProfileResponse))
print(customerUserProfileResponse)
# print(customerUserProfileResponse.data)









class DataBean(object):
    def __init__(self, lastLoginTime, id, baseCurrency, userName):
        self.lastLoginTime = lastLoginTime
        self.id = id
        self.baseCurrency = baseCurrency
        self.userName = userName

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id


    def setLastLoginTime(self, lastLginTime):
        self.lastLginTime = lastLginTime

    def getLastLoginTime(self):
        return self.lastLginTime


    def setBaseCurrency(self, baseCurrency):
        self.baseCurrency = baseCurrency

    def getBaseCurrency(self):
        return self.baseCurrency


    def setUserName(self, userName):
        self.userName = userName

    def getUserName(self):
        return self.userName

def dict2DataBean(d):
    return DataBean(d['lastLoginTime'], d['id'], d['baseCurrency'], d['userName'])


json_str1 = '{"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"}'
print(type(json_str1))
dataBean = json.loads(json_str1, object_hook=dict2DataBean)
print('dataBean的类型为：%s' % type(dataBean))
print(dataBean.userName)

import json
import pymysql


def get_data():
    with open('./camera.json', 'r') as f:
        camera_text = json.load(f)  # 解析每一行数据
    return camera_text


def data_insert(camera_text):
    db = pymysql.connect("localhost", "root", "123456", "filestore")
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
    insert_ca = "insert into camera(date,type,description,CIDlocation,IDproject,IDtask,IDcamera,mu,value_x,value_y,ext_info)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

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
    a = get_data()
    data_insert(a)