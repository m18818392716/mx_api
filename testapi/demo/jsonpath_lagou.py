# jsonpath_lagou.py

import urllib3
import jsonpath
import json
import chardet

from urllib import request
from urllib import parse
from urllib.request import urlopen



# json.loads() 是把 Json格式字符串解码转换成Python对象，如果在json.loads的时候出错，要注意被解码的Json字符的编码。
# 如果传入的字符串的编码不是UTF-8的话，需要指定字符编码的参数 encoding

# dataDict = json.loads(jsonStrGBK);
#
# dataJsonStr是JSON字符串，假设其编码本身是非UTF-8的话而是GBK 的，那么上述代码会导致出错，改为对应的：
# dataDict = json.loads(jsonStrGBK, encoding="GBK");
#
# 如果 dataJsonStr通过encoding指定了合适的编码，但是其中又包含了其他编码的字符，则需要先去将dataJsonStr转换为Unicode，然后再指定编码格式调用json.loads()
# dataJsonStrUni = dataJsonStr.decode("GB2312"); dataDict = json.loads(dataJsonStrUni, encoding="GB2312");


values = {'username': '962457839@qq.com', 'password': 'XXXX'}
data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型


url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
request = request.Request(url)
response = urlopen(request)
html = response.read()
print (html.decode())



# 把json格式字符串转换成python对象
jsonobj = json.loads(html)

# 从根节点开始，匹配name节点
citylist = jsonpath.jsonpath(jsonobj, '$..name')

print (citylist)
print (type(citylist))
fp = open('city.json', 'w')

content = json.dumps(citylist, ensure_ascii=False)
print (content)

fp.write(content.encode('utf-8'))
fp.close()