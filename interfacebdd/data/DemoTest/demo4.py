#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 下午12:31
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo4.py
# @Software: PyCharm

import json

class Man():

    def __init__(self, d):
        self.code = d['code']
        self.message = d['message']
        # self.data = d['data']

    def setCode(self, code):
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

    # def __init__(self, code, message):
    #     self.code = code
    #     self.message = message

json_str = '{"code": 29, "message": "tom"}'
# json_str = '{"code": "0", "message": "success", "data": {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"}}'


# def handle(d):
#     # return Man(d['code'], d['message'], json.dumps(d['data'].__dict__))
#     return Man(d)

m = json.loads(json_str, object_hook=Man)

print(m)
print(type(m))
print('code: %s' % m.code)
print('code type is: %s' % type(m.code))
print('message: %s' % m.message)
print('message type is: %s' % type(m.message))
print('data: %s' % m.data)
print('data type is: %s' % type(m.data))

# print(json.dumps(m.data.__dict__))
# print()