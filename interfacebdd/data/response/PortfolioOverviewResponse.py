#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午12:23
# @Author  : Susanna Chen
# @Site    : 
# @File    : PortfolioOverviewResponse.py
# @Software: PyCharm

class PortfolioOverviewResponse(object):
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
        def __init__(self, portfolios):
            self.portfolios = portfolios

        def getPortfolios(self):
            return self.portfolios

        class Portfolio(object):
            def __init__(self, externalId, currency, name, amount, id, liabilitiesAmount, liabilitiesCurrency, netAssetsAmount, netAssetsCurrency, ytd, updateDate):
                self.externalId = externalId
                self.currency = currency
                self.name = name
                self.amount = amount
                self.id = id
                self.liabilitiesAmount = liabilitiesAmount
                self.liabilitiesCurrency = liabilitiesCurrency
                self.netAssetsAmount = netAssetsAmount
                self.netAssetsCurrency = netAssetsCurrency
                self.ytd = ytd
                self.updateDate = updateDate

            def getExternalId(self):
                return self.externalId

            def getCurrency(self):
                return self.currency

            def getName(self):
                return self.name

            def getAmount(self):
                return self.amount

            def getId(self):
                return self.id

            def getLiabilitiesAmount(self):
                return self.liabilitiesAmount

            def getLiabilitiesCurrency(self):
                return self.liabilitiesCurrency

            def getNetAssetsAmount(self):
                return self.netAssetsAmount

            def getNetAssetsCurrency(self):
                return self.liabilitiesCurrency

            class Ytd(object):
                def __init__(self, amount, currency, weight, date):
                    self.amount = amount
                    self.currency = currency
                    self.weight = weight
                    self.date = date

                def getAmount(self):
                    return self.amount

                def getCurrency(self):
                    return self.currency

                def getWeight(self):
                    return self.weight

                def getDate(self):
                    return self.date



