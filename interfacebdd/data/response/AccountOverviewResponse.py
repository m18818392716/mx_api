#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午12:22
# @Author  : Susanna Chen
# @Site    : 
# @File    : AccountOverviewResponse.py
# @Software: PyCharm

class AccountOverviewResponse(object):
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

        def __init__(self, accounts):
            self.accounts = accounts

        def getAccounts(self):
            return self.accounts

        class Account(object):

            def __init__(self, id, name, amount, externalId, currency, liabilitiesAmount, liabilitiesCurrency,
                         netAssetsAmount, netAssetsCurrency, updateDate, ytd):
                self.id = id
                self.name = name
                self.amount = amount
                self.externalId = externalId
                self.currency = currency
                self.liabilitiesAmount = liabilitiesAmount
                self.liabilitiesCurrency = liabilitiesCurrency
                self.netAssetsAmount = netAssetsAmount
                self.netAssetsCurrency = netAssetsCurrency
                self.updateDate = updateDate
                self.ytd = ytd

            def getId(self):
                return self.id

            def getName(self):
                return self.currency

            def getAmount(self):
                return self.amount

            def getExternalId(self):
                return self.externalId

            def getCurrency(self):
                return self.currency

            def getLiabilitiesAmount(self):
                return self.liabilitiesAmount

            def getLiabilitiesCurrency(self):
                return self.liabilitiesCurrency

            def getNetAssetsAmount(self):
                return self.netAssetsAmount

            def getNetAssetsCurrency(self):
                return self.netAssetsCurrency

            class Ytd(object):
                def __init__(self, amount, currency, weight):
                    self.amount = amount
                    self.currency = currency
                    self.weight = weight

                def getAmount(self):
                    return self.amount

                def getCurrency(self):
                    return self.currency

                def getWeight(self):
                    return self.weight
