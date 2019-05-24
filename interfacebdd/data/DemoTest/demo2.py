#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午6:21
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm

import json
import requests

class CustomerUserProfileResponse(object):
    # age = 10

    # def __init__(self, code, message, data):
    def __init__(self):
    #     self.__dict__ = d
    #     self.code = None
    #     self.message = None
    #     self.data = None
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
    # return CustomerUserProfileResponse(d['code'], d['message'], d['data'])
    return CustomerUserProfileResponse()


dict_headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": r"application/json;charset=UTF-8"}
url = "https://proj.gtomato.com.cn/mobile/v1/customer/userprofile"
response = requests.get(url, headers=dict_headers)
print(type(response.json()))
print(type(json.dumps(response.json())))
print(response.json())
print(json.dumps(response.json()))


json_str = json.dumps(response.json())
userProfile = CustomerUserProfileResponse()


userProfile.setCode(response.json()['code'])
userProfile.setMessage(response.json()['message'])
userProfile.setData(response.json()['data'])

print(userProfile.getCode())
print(userProfile.getMessage())
print(userProfile.getData())



customerUserProfileResponse = json.loads(json_str, object_hook=dict2CustomerUserProfileResponse)

print(type(customerUserProfileResponse))
print(type(customerUserProfileResponse.__dict__))
print(customerUserProfileResponse.data)

# print(customerUserProfileResponse.data)
# print(customerUserProfileResponse.data.id)
# print(customerUserProfileResponse.data.baseCurrency)