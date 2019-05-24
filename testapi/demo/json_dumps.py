# json_dumps.py

import json
import chardet

# chardet是一个非常优秀的编码识别模块，可通过pip进行安装

# json.dumps()
# 实现python类型转化为json字符串,返回一个str对象 把一个Python对象编码转换成Json字符串
# 从python原始类型向json的转化对照如下：

# Python         JSON
# dict           object
# list,tuple     array
# str,unicode    string
# int,long,float number
# True           true
# False          false
# None           null

listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)

dictStr = {"city": "北京", "name": "大猫"}

# json.dumps(listStr)
# # '[1, 2, 3, 4]'
# json.dumps(tupleStr)
# # '[1, 2, 3, 4]'

# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
# chardet.detect()返回字典, 其中confidence是检测精确度

json.dumps(dictStr)
# '{"city": "\\u5317\\u4eac", "name": "\\u5927\\u5218"}'

result = chardet.detect(json.dumps(dictStr).encode())
print (result)
# {'confidence': 1.0, 'encoding': 'ascii'}

print (json.dumps(dictStr, ensure_ascii=False))
# {"city": "北京", "name": "大刘"}

result1 = chardet.detect(json.dumps(dictStr, ensure_ascii=False).encode())
print (result1)
# {'confidence': 0.99, 'encoding': 'utf-8'}

