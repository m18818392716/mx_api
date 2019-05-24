#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 下午2:08
# @Author  : Susanna Chen
# @Site    : 
# @File    : jsonToObjectAndObjectToJson.py
# @Software: PyCharm
import json

class user:
    def __init__(self, name, pwd, data):
        self.name = name
        self.pwd = pwd
        self.data = data

    def getName(self):
        return self.name

    def getPwd(self):
        return self.pwd

    def getData(self):
        return self.data

    def __str__(self):
        return 'user(' + self.name + ',' + self.pwd +',' + str(self.data) + ')'

#重写JSONEncoder的default方法，object转换成dict
class userEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, user):
            return {
                'name': o.name,
                'pwd': o.pwd,
                'data': o.data
            }
        return json.JSONEncoder.default(o)

#重写JSONDecoder的decode方法，dict转换成object

class userDecode(json.JSONDecoder):
    def decode(self, s):
        dic = super().decode(s)
        return user(dic['name'], dic['pwd'], dic['data'])

#重写JSONDecoder的__init__方法，dict转换成object
class userDecode2(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=dic2objhook)


# 对象转换成dict
def obj2dict(obj):

    if (isinstance(obj, user)):
        return {
            'name': obj.name,
            'pwd': obj.pwd,
            'data': obj.data
        }
    else:
        return obj

# dict转换为对象
def dic2objhook(dic):

    if isinstance(dic, dict):
        return user(dic['name'], dic['pwd'], dic['data'])
    return dic

# 第一种方式，直接把对象先转换成dict
u = user('smith', '123456', {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"})
uobj = json.dumps(obj2dict(u))
print('uobj: ', uobj)


#第二种方式，利用json.dumps的关键字参数default
u = user('smith', '123456', {"lastLoginTime": 1533882667, "id": "5", "baseCurrency": "GBP", "userName": "Jones"})
uobj2 = json.dumps(u, default=obj2dict)
print('uobj2: ', uobj)

#第三种方式，定义json的encode和decode子类，使用json.dumps的cls默认参数
user_encode_str = json.dumps(u, cls=userEncoder)
print('user2json: ', user_encode_str)






#json转换为object
u2 = json.loads(user_encode_str, cls=userDecode)
print('json2user type is: %s' % type(u2))
print('json2user: ', u2)
print('json2user-->name: ', u2.getName())
print('json2user-->pwd: ', u2.getPwd())
print('json2user-->data: ', u2.getData())



#另一种json转换成object的方式
# u3 = json.loads(user_encode_str, cls=userDecode2)
# print('json2user2 type is: %s' % type(u3))
# print('json2user2: ', u3)
# print('json2user-->name: ', u3.getName())
# print('json2user-->pwd: ', u3.getPwd())