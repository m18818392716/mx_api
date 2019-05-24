# -*- coding: utf-8 -*-
# @Author  : leizi
import os,datetime,time
from myapp.testCase.case import *
from myapp.Public.py_Html import createHtml
from myapp.Public.get_excel import datacel
from  myapp.Public.Dingtalk import send_ding
from myapp.Public.BSTestRunner import BSTestRunner
import unittest

# 此py文件运行方式是python

test_dir='./testCase'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="case.py")
print(discover)
suite = unittest.TestSuite()
suite.addTests(discover)

if __name__ == '__main__':

    report_dir ='./test_bstestrunner_Report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir +'/'+now +'.html'

    # 使用with打开文件后可以不用close文件
    with open(report_name,'wb')as f:

        runner = unittest.TextTestRunner()
        runer = BSTestRunner(stream=f, title="Test Report", description='Test case result')
        runer.run(suite)