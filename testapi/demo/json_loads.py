# json_loads.py

import json
# json模块提供了四个功能：dumps、dump、loads、load，用于字符串和python数据类型间进行转换

# json.loads()
# 把Json格式字符串解码转换成Python对象，从json到python的类型转化对照如下：

# JSON          Python
# object        dict
# array         list
# string        unicode
# number(int)   int,long
# number(real)  float
# true          True
# false         False
# null          None

strList = '[1, 2, 3, 4]'

strDict = '{"city": "北京", "name": "大猫"}'

json.loads(strList)
# [1, 2, 3, 4]

json.loads(strDict)  # json数据自动按Unicode存储
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u732b'}