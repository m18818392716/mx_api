#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 上午11:14
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo3.py
# @Software: PyCharm

import json


class Man(object):

    code = None
    message = None
    data = None

    # def __init__(self, code, message, data):
    #     self.code = code
    #     self.message = message
    #     self.data = data

    def __init__(self, d):
        self.__dict__ = d
        # self.code = None
        # self.message = None
        # self.data = None

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

    class Woman(object):

        # def __init__(self, lastLoginTime, id, baseCurrency, userName):
        #
        #     self.lastLoginTime = lastLoginTime
        #     self.id = id
        #     self.baseCurrency = baseCurrency
        #     self.userName = userName

        def __init__(self, d):
            self.__dict__ = d




# json_str = '{"code": 29, "message": "tom"}'
json_str = '{"code": "0", "message": "success", "data": {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"}}'

def handle(d):
    # return Man(d['code'], d['message'], d['data'].__dict)
    return Man(d)
    # return Man(d['code'], d['message'])


def handle1(d):
    # return Man.Woman(d['lastLoginTime'], d['id'], d['baseCurrency'], d['userName'])
    return Man.Woman(d)

m = json.loads(json_str, object_hook=handle)

print(m)
print(type(m))
print('code: %s' % m.code)
print('code type is: %s' % type(m.code))
print('message: %s' % m.message)
print('message type is: %s' % type(m.message))
print('data: %s' % m.data)
print('data type is: %s' % type(m.data))
print(json.dumps(m.data.__dict__))
print()

d = {}
man = Man(d)
man.setCode(m.code)
man.setMessage(m.message)
man.setData(m.data.__dict__)
print(man.getCode())
print(man.getMessage())
print(man.getData())
#
# woman = Man.Woman(d)



print()
json_str1 = json.dumps(m.data.__dict__)
n = json.loads(json_str1, object_hook=handle1)
print(n)
print(type(n))
print('lastLoginTime: %s' % n.lastLoginTime)
print('lastLoginTime type is: %s' % type(n.lastLoginTime))
print('id: %s' % n.id)
print('id type is: %s' % type(n.id))
print('baseCurrency: %s' % n.baseCurrency)
print('baseCurrency type is: %s' % type(n.baseCurrency))
print('userName: %s' % n.userName)
print('userName type is: %s' % type(n.userName))
