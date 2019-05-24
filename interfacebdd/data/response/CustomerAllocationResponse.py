#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 下午5:27
# @Author  : Susanna Chen
# @Site    : 
# @File    : CustomerAllocationResponse.py
# @Software: PyCharm

class CustomerAllocationResponse(object):
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
        def __init__(self, clazz, currency, region):
            self.clazz = clazz
            self.currency = currency
            self.region = region

        def getClazz(self):
            return self.clazz

        def getCurrency(self):
            return self.currency

        def getRegion(self):
            return self.region

        class Clazz(object):
            def __init__(self, id, amount, name, weigt, currency, nodes, donutWeight):
                self.id = id
                self.amount = amount
                self.name = name
                self.weigt = weigt
                self.currency = currency
                self.nodes = nodes
                self.donutWeight = donutWeight

            class Node(object):
                def __init__(self, id, amount, name, currency, weight):
                    self.id = id
                    self.amount = amount
                    self.name = name
                    self.currency = currency
                    self.weight = weight

        class Currency(object):
            def __init__(self, id, amount, name, currency, weight, donutWeight):
                self.id = id
                self.amount = amount
                self.name = name
                self.currency = currency
                self.weight = weight
                self.donutWeight = donutWeight

        class Region(object):
            def __init__(self, id, amount, name, currency, weight, donutWeight):
                self.id = id
                self.amount = amount
                self.name = name
                self.currency = currency
                self.weight = weight
                self.donutWeight = donutWeight