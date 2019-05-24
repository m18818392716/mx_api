# json_load.py

import json

strList = json.load(open("listStr.json"))
print (strList)

# [{u'city': u'\u5317\u4eac'}, {u'name': u'\u5927\u5218'}]

strDict = json.load(open("dictStr.json"))
print (strDict)
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u5218'}