#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 下午5:44
# @Author  : Susanna Chen
# @Site    : 
# @File    : CustomerRateResponse.py
# @Software: PyCharm

class CustomerRateResponse(object):
    def __init__(self, code, message, data):
        self.code = code
        self.message = message
        self.data = data

        def getCode(self):
            return self.code

        def getMessage(self):
            return self.message

        def getData(self):
            return self.data

    class DataBean(object):
        def __init__(self, base):
            self.base = base

        def getBase(self):
            return self.base


        class Base(object):
            def __init__(self, code, rate):
                self.code = code
                self.rate = rate

            def getCode(self):
                return self.code

            def getRate(self):
                return self.rate
