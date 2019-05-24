#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午12:22
# @Author  : Susanna Chen
# @Site    : 
# @File    : CustomerUserProfileResponse.py
# @Software: PyCharm
import json
import requests

class CustomerUserProfileResponse(object):
    # age = 10

    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data
        print("调用父类有参构造函数")

    # def getAge(self):
    #     if CustomerUserProfileResponse.age < 1:
    #         return 1
    #     else:
    #         return CustomerUserProfileResponse.age
    #
    # def setAge(self, value):
    #     if value > 2: value = 2
    #     self.age = value

    def getCode(self):
        return self.code

    def getMessage(self):
        return self.message

    def getData(self):
        return self.data

    class DataBean(object):

        def __init__(self, lastLoginTime, id, baseCurrency, userName):
            self.lastLoginTime = lastLoginTime
            self.id = id
            self.baseCurrency = baseCurrency
            self.userName = userName

        def getId(self):
            return self.id

        def getLastLoginTime(self):
            return self.lastLoginTime

        def getBaseCurrency(self):
            return self.baseCurrency

        def getUserName(self):
            return self.userName

class userDecode(json.JSONDecoder):
    def decode(self, s):
        dic = super().decode(s)
        return CustomerUserProfileResponse(dic['code'], dic['message'], dic['data'])

class dataDecode(json.JSONDecoder):
    def decode(self, s):
        dic = super().decode(s)
        return CustomerUserProfileResponse.DataBean(dic['lastLoginTime'], dic['id'], dic['baseCurrency'], dic['userName'])


def dict2CustomerUserProfileResponse(d):
    return CustomerUserProfileResponse(d['code'], d['message'], d['data'])

dict_headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": r"application/json;charset=UTF-8"}
url = "https://proj.gtomato.com.cn/mobile/v1/customer/userprofile"
response = requests.get(url, headers=dict_headers)
print(type(response.json()))
print(type(json.dumps(response.json())))
print(response.json())
print(json.dumps(response.json()))
json_str = json.dumps(response.json())
# json_str = '{"code":"0","message":"success","data":{"lastLoginTime":1533882667,"id":"5","baseCurrency":"GBP","userName":"Jones"}}'
# customerUserProfileResponse = json.loads(json_str, object_hook=dict2CustomerUserProfileResponse)

customerUserProfileResponse = json.loads(json_str, cls=userDecode)


print(type(customerUserProfileResponse))

print(customerUserProfileResponse.getCode())
print(customerUserProfileResponse.getMessage())
print('data type is: %s' % type(customerUserProfileResponse.getData()))
print('data: %s' % customerUserProfileResponse.getData())

print(customerUserProfileResponse.data['id'])
print(customerUserProfileResponse.data['baseCurrency'])

# json_str1 = '{"lastLoginTime":1533882667,"id":"5","baseCurrency":"GBP","userName":"Jones"}'
json_str1 = json.dumps(customerUserProfileResponse.getData())
print('json_str1 type is: %s' % type(json_str1))
print('json_str1 is: %s' % json_str1)
dataBean = json.loads(json_str1, cls=dataDecode)

print(type(dataBean))

print(dataBean.getLastLoginTime())
print(dataBean.getId())
print(dataBean.getBaseCurrency())
print(dataBean.getUserName())










# d = {'username': 'susanna'}
# userProfile = CustomerUserProfileResponse()
#
#
# userProfile.setCode(customerUserProfileResponse.code)
# userProfile.setMessage(customerUserProfileResponse.message)
#
# print(userProfile.getCode())
# print(userProfile.getMessage())
# class DataBean(object):
#     def __init__(self):
#         self.lastLoginTime = None
#         self.id = None
#         self.baseCurrency = None
#         self.userName = None
#
#     def setId(self, id):
#         self.id = id
#
#     def getId(self):
#         return self.id
#
#
#     def setLastLoginTime(self, lastLginTime):
#         self.lastLginTime = lastLginTime
#
#     def getLastLoginTime(self):
#         return self.lastLginTime
#
#
#     def setBaseCurrency(self, baseCurrency):
#         self.baseCurrency = baseCurrency
#
#     def getBaseCurrency(self):
#         return self.baseCurrency
#
#
#     def setUserName(self, userName):
#         self.userName = userName
#
#     def getUserName(self):
#         return self.userName