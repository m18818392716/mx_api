# json_dump.py
# 将Python内置类型序列化为json对象后写入文件

import json

listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr, open("listStr.json", "w"), ensure_ascii=False)

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json", "w"), ensure_ascii=False)