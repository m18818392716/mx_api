# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  : lileilei
# @Site    :
# @File    : testFengzhuang.py
from myapp.Public.test_requests import requ
import unittest

reques=requ()
class TestApi(object):
	def __init__(self,url, key, connent, fangshi, header):
		self.url = url
		self.key = key
		self.header = header
		self.connent = connent
		self.fangshi = fangshi
	def testapi(self):

		if self.fangshi == 'POST':
			self.parem = self.connent

			self.response = reques.post(self.url,json=self.parem, headers=self.header)
			# self.response = reques.post(self.url,self.header, self.parem)

		elif self.fangshi == "GET":
			self.parem = {'key': self.key, 'info': self.connent}

			# self.response = reques.get(url=self.url,headers=self.header, params=self.parem)
			self.response = reques.get(url=self.url, headers=self.header,params=self.parem)

		return self.response

	def getJson(self):
		json_data = self.testapi()
		return json_data