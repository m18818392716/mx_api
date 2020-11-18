import requests
from openpyxl import Workbook
KeyWord = "python"
url = "https://www.lagou.com/jobs/list_" + KeyWord + "?&cl=false&fromSearch=true&labelWords=&suginput="
url_GetJob = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36",
    "Referer": url
}

# 创建会话
session = requests.session()
res1 = session.get(url, headers=headers, verify=False)
# 保持会话提交表单
data = {
    "first": "true",
    "pn": "1",
    "kd": KeyWord
}
res = session.post(url_GetJob, headers=headers, data=data, verify=False).json()
print(res)
list_con = res['content']['positionResult']['result']
info_list = []
for i in list_con:
    info = []
    info.append(i['companyId'])
    info.append(i['companyFullName'])
    info.append(i['companyShortName'])
    info.append(i['companySize'])
    info.append(str(i['companyLabelList']))

    info.append(i['industryField'])
    info.append(i['financeStage'])

    info.append(i['positionId'])
    info.append(i['positionName'])
    info.append(i['positionAdvantage'])
    #         info.append(i['positionLables'])

    info.append(i['city'])
    info.append(i['district'])
    #         info.append(i['businessZones'])

    info.append(i['salary'])
    info.append(i['education'])
    info.append(i['workYear'])
    info_list.append(info)

info_result = []
title = ['公司ID', '公司全名', '公司简称', '公司规模', '公司标签', '行业领域', '融资情况', "职位编号", "职位名称", "职位优势", "城市", "区域", "薪资水平", '教育程度',
         "工作经验"]
info_result.append(title)

info_result = info_result + info_list
# 写入excel文件
wb = Workbook()
ws1 = wb.active
ws1.title = KeyWord
for row in info_result:
    ws1.append(row)
wb.save('haha.xlsx')

