# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:35
# @Author  : lileilei
# @File    : get_excel.py
import xlrd
from myapp.Public.log import LOG,logger

@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[1]
        nrows=me.nrows
        listid=[]
        listkey=[]
        listheader=[]
        listconeent=[]
        listurl=[]
        listfangshi=[]
        listqiwang=[]
        listrelut=[]
        listname=[]
        for i in range(1,nrows):
            listid.append(me.cell(i,0).value)
            listkey.append(me.cell(i,2).value)
            listheader.append(me.cell(i,3).value)
            listconeent.append(me.cell(i,4).value)
            listurl.append(me.cell(i,5).value)
            listname.append(me.cell(i,1).value)
            listfangshi.append((me.cell(i,6).value))
            listqiwang.append((me.cell(i,7).value))
        return listid,listkey,listheader,listconeent,listurl,listfangshi,listqiwang,listname
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return

@logger('解析测试用例文件')
def datacel1(filrpath):
    try:
        # listid, listurl, listheader,listinterface, listmeth, listfobject, listparam, listassert
        file=xlrd.open_workbook(filrpath)
        me=file.sheets()[0]
        nrows=me.nrows
        listid=[]
        listurl=[]
        listheader=[]
        listinterface=[]
        listmeth=[]
        listfobject=[]
        listparam=[]
        listassert=[]
        # listrelut=[]
        for i in range(1,nrows):
            listid.append(me.cell(i,0).value)
            listurl.append(me.cell(i,1).value)
            listheader.append(me.cell(i,2).value)
            listinterface.append(me.cell(i,3).value)
            listmeth.append(me.cell(i,4).value)
            listfobject.append(me.cell(i,5).value)
            listparam.append((me.cell(i,6).value))
            listassert.append((me.cell(i,7).value))
        return listid, listurl, listheader,listinterface, listmeth, listfobject, listparam, listassert
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s'%e)
        return