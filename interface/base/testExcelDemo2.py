import requests, json
from openpyxl import Workbook

# http请求头信息
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '67',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'user_trace_token=20201118213833-0c435b24-5e4f-4b93-b06f-1c1acd1087ef; _ga=GA1.2.1236145479.1605706719; LGSID=20201118213839-aa88b61e-04a7-4a91-b331-5552d415c755; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.060000jpQS8OmQtLPbexVpzOQnATomZawuLW%5FgfrRNm359GAsOXcYszZQGMZ34Xpn9ngEb3t2yZsOpTU6dg0vIIigZZeTkO9t8Rt9pUtdVa4GK5nciIR79xPB59HnTcUmIAZ602Bw4rDgnNhuSRLyWFgHYqbBWqGKd9F5ydJnHKX6DC65P8QR31i-gACbEbKxRH3TgHueUn6s2jwddiANYzEK%5FdR.7Y%5FNR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt%5FrE-9kYryqM764TTPqKi%5FnYQZHuukL0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqs2v4%5FtL30ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5TaV8UHPSnx1do00ThPv5HD0IgF%5Fgv-b5HDdnWcYrjRdnjn0UgNxpyfqnHn3P1nLnHf0UNqGujYknjT4PWcvP6KVIZK%5Fgv-b5HDkPHnY0ZKvgv-b5H00pywW5R9rffKWThnqPW0dnH6%26ck%3D2272.3.144.389.153.237.151.378%26dt%3D1605706709%26wd%3D%25E6%258B%2589%25E9%2592%25A9%25E7%25BD%2591%26tpl%3Dtpl%5F11534%5F23295%5F19442%26l%3D1522485503%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520-%252520%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%25258B%252589%2525E5%25258B%2525BE%21%2526linkType%253D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpt%5Fbaidu%5Fpcbt; LGUID=20201118213839-42f6dae7-9a84-4864-962b-cf3203deb477; _gid=GA1.2.1773384236.1605706848; sajssdk_2015_cross_new_user=1; gate_login_token=11b568b7e7f53812dab72fea2889c02bb74e49101c1ec94e; LG_LOGIN_USER_ID=3be421a504b6f67bf626a400f1a74823a8b5d3e1c3f461e5; LG_HAS_LOGIN=1; _putrc=2292E575821C3BDB; JSESSIONID=ABAAAECAAEBABIIF6653008FA0BF6F6190306303F447AED; login=true; unick=%E9%99%88%E5%8D%83; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=14; index_location_city=%E5%B9%BF%E5%B7%9E; WEBTJ-ID=20201118214117-175db968aca6ec-0262d3380cf765-930346c-2073600-175db968acb2e3; RECOMMEND_TIP=true; sensorsdata2015session=%7B%7D; privacyPolicyPopup=false; X_MIDDLE_TOKEN=2f9913d8db84efcfcf54e32ab219b024; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1605706719,1605707363; X_HTTP_TOKEN=075e29b902d2b88b754707506171e43b4d46bf5370; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%229981434%22%2C%22%24device_id%22%3A%22175db9619dd78d-0668f2b1ba5532-930346c-2073600-175db9619dea99%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2286.0.4240.198%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22first_id%22%3A%22175db9619dd78d-0668f2b1ba5532-930346c-2073600-175db9619dea99%22%7D; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1605707456; LGRID=20201118215057-81e2b73d-0a54-4144-a0f1-a8ad86cf22c6; SEARCH_ID=0ae94fe53749451d9d1380bff87a1a73',
    'authority': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_web%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_json(url, page, lang_name):
    data = {'first': "true", 'pn': page, 'kd': lang_name, 'city': "广州"}

    # POST请求
    print(url)
    json = requests.post(url, data, headers=headers).json()
    print(json)
    list_con = json['content']['positionResult']['result']
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
    return info_list


def main():
    lang_name = input('职位名：')
    page = 1
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    info_result = []
    title = ['公司ID', '公司全名', '公司简称', '公司规模', '公司标签', '行业领域', '融资情况', "职位编号", "职位名称", "职位优势", "城市", "区域", "薪资水平", '教育程度',
             "工作经验"]
    info_result.append(title)

    # 遍历网址
    while page < 31:
        info = get_json(url, page, lang_name)
        info_result = info_result + info
        page += 1
        # 写入excel文件
        wb = Workbook()
        ws1 = wb.active
        ws1.title = lang_name
        for row in info_result:
            ws1.append(row)
        wb.save('职位信息3.xlsx')


main()