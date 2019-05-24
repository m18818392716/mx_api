#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午4:05
# @Author  : Susanna Chen
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

import json
import demjson

class Response:

    def __init__(self, status, info, data) -> None:
        super().__init__()
        self.status = status
        self.info = info
        self.data = data

    @staticmethod
    def object_hook(d):
        return Response(d['status'], d['info'], d['data'])


body = '{"status":1,"info":"发布成功","data":{"id":"52","feed_id":"70"}}'
# resp = json.loads(body, object_hook=Response.object_hook)
# resp = demjson.decode(body, encoding='utf-8', encode_dict=Response.object_hook)
# print(resp)
# print(type(resp))


class DemoTest:
    def __init__(self, d):
        self.__dict__ = d

s = '{"status":1,"info":"发布成功","data":{"id":"52","feed_id":"70"}}'
data = json.loads(s, object_hook=DemoTest)
print(type(data))

print(data.status)
print(data.info)

print(data.data)
print(type(data.data))
print(json.dumps(data.data.__dict__))
print(type(json.dumps(data.data.__dict__)))

print(data.data.id)
print(data.data.feed_id)