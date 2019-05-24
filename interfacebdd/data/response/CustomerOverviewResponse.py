#-*- coding:utf-8 -*-
# @Time    : 2019/4/2 下午12:23
# @Author  : Susanna Chen
# @Site    : 
# @File    : CustomerOverviewResponse.py
# @Software: PyCharm
class CustomerOverviewResponse(object):

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

        def __init__(self, customer, ytd, hasLiabilities, newDocumentCount):
            self.customer = customer
            self.ytd = ytd
            self.hasLiabilities = hasLiabilities
            self.newDocumentCount = newDocumentCount

        def getCustomer(self):
            return self.customer

        def getYtd(self):
            return self.ytd

        def getHasLiabilities(self):
            return self.hasLiabilities

        def getNewDocumentCount(self):
            return self.newDocumentCount

        class Customer(object):

            def __init__(self, name, account, currency, bookingCenter, updateDate, liabilitiesAmount, liabilitiesCurrency, netAssetsAmount, netAssetsCurrency):
                self.name = name
                self.account = account
                self.currency = currency
                self.bookingCenter = bookingCenter
                self.updateDate = updateDate
                self.liabilitiesAmount = liabilitiesAmount
                self.liabilitiesCurrency = liabilitiesCurrency
                self.netAssetsAmount = netAssetsAmount
                self.netAssetsCurrency = netAssetsCurrency

            def getName(self):
                return self.name

            def getAccount(self):
                return self.account

            def getCurrency(self):
                return self.currency

            def getBookingCenter(self):
                return self.bookingCenter

            def getUpdateDate(self):
                return self.updateDate

            def getLiabilitiesAmount(self):
                return self.liabilitiesAmount

            def getLiabilitiesCurrency(self):
                return self.liabilitiesCurrency

            def getNetAssetsAmount(self):
                return self.netAssetsAmount

            def getNetAssetsCurrency(self):
                return self.netAssetsCurrency


        class Ytd(object):
            def __init__(self, amount, currency):
                self.amount = amount
                self.currency = currency

            def getAmount(self):
                return self.amount

            def getCurrency(self):
                return self.currency