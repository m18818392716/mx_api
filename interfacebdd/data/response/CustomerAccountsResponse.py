
#-*- coding:utf-8 -*-
# @Time    : 2019/4/3 下午5:17
# @Author  : Susanna Chen
# @Site    : 
# @File    : CustomerAccountsResponse.py
# @Software: PyCharm

class CustomerAccountsResponse(object):
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
        def __init__(self, accounts, totalSize):
            self.accounts = accounts
            self.totalSize = totalSize

        def getAccounts(self):
            return self.accounts

        def getTotalSize(self):
            return self.totalSize

        class Acocunt(object):
            def __init__(self, id, name, weight, amount, externalId, currency, baseCurrency):
                self.id = id
                self.name = name
                self.weight = weight
                self.amount = amount
                self.externalId = externalId
                self.currency = currency
                self.baseCurrency = baseCurrency

            def getId(self):
                return self.id

            def getName(self):
                return self.name

            def getWeight(self):
                return self.weight

            def getAmount(self):
                return self.amount

            def getExternalId(self):
                return self.externalId

            def getCurrency(self):
                return self.currency

            def getBaseCurrency(self):
                return self.baseCurrency