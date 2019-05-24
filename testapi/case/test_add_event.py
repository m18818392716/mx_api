# coding:utf-8
import unittest
import requests
import os, sys
import testapi.base.requestHeaders as requestHeader

from django.conf import settings

# 此python文件的运行方式为python test

# 设置Django运行锁依赖的环境，DemoTest1为项目文件名，settings是项目的配置文件
import os,django
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DemoTest1.settings')

# django.setup()


cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cur_path)
from testapi.db_fixture import test_data

headers = {}

class TestAddEvent(unittest.TestCase):
    """添加发布会"""

    def setUp(self):

        # customer userprofile Get请求
        self.base_url = settings.BASE_URL + "/mobile/v1/customer/userprofile"

        # customer overview Get请求
        self.customer_overview = settings.BASE_URL + "/mobile/v1/customer/5/overview?currency=GBP"

        # customer accounts Get请求
        self.customer_accounts = "https://proj.gtomato.com.cn/mobile/v1/customer/6/accounts?currency=GBP&limit=100"

        # customer allocation Get请求
        self.customer_allocation = "https://proj.gtomato.com.cn/mobile/v1/customer/6/allocation?currency={{customerCurrency}}&category=ALL"

        # customer rate Get请求
        self.customer_rate = "https://proj.gtomato.com.cn/mobile/v1/customer/5/xrate"

        # customer allocation holdings Get请求
        self.customer_allcation_holdings = "https://proj.gtomato.com.cn/mobile/v1/customer/4/holdings/allocation?category=currency&categoryId=8,9&limit=15&currency={{customerCurrency}}"

        # customer allocation holding group Get请求
        self.customer_allocation_holding_group = "https://proj.gtomato.com.cn/mobile/v1/customer/4/holdings/allocation/group?category=asset&categoryId=4_1&offset=0&limit=15&currency={{customerCurrency}}"

        # customer documents Post请求
        self.customer_documents = settings.BASE_URL + "/mobile/v1/customer/5/documents"

        # customer documents accounts Get请求
        self.customer_documents_accounts = "https://proj.gtomato.com.cn/mobile/v1/customer/1/documents/accounts"

        # customer documents categories Get请求
        self.customer_documents_categories = "https://proj.gtomato.com.cn/mobile/v1/customer/2/documents/categories"

        # customer documents flag Post请求
        self.documents_flag = "https://proj.gtomato.com.cn/mobile/v1/customer/1/documents/flag"




        # account overview Post请求
        self.account_overview = "https://proj.gtomato.com.cn/mobile/v1/account/overview"

        # account portfolios Get请求
        self.account_portfolios = "https://proj.gtomato.com.cn/mobile/v1/account/1/portfolios?currency=USD&limit=200"

        # account allocation Get请求
        self.account_allocation = "https://proj.gtomato.com.cn/mobile/v1/account/1/allocation?currency=USD&category=ALL"

        # account rate Get请求
        self.account_rate = "https://proj.gtomato.com.cn/mobile/v1/account/5/xrate"

        # account allocation holdings Get请求
        self.account_allocation_holdings = "https://proj.gtomato.com.cn/mobile/v1/account/4/holdings/allocation?category=Currency&categoryId=4&offset=0&limit=15&currency=gbp"

        # account allocation holding group Get请求
        self.account_allocation_holding_group = "https://proj.gtomato.com.cn/mobile/v1/account/4/holdings/allocation/group?category=asset&categoryId=4_1&offset=15&currency=GBP"




        # portfolios overview Post请求
        self.portfolio_overview = "https://proj.gtomato.com.cn/mobile/v1/portfolio/overview"

        # portfolio holdings Get请求
        self.portfolio_holdings = "https://proj.gtomato.com.cn/mobile/v1/portfolio/2/holdings?currency=USD"

        # portfolio allocation Get请求
        self.portfolio_allocation = "https://proj.gtomato.com.cn/mobile/v1/portfolio/2/allocation?currency=JPY&category=ALL"

        # portfolio transaction Get请求
        self.portfolio_transaction = "https://proj.gtomato.com.cn/mobile/v1/portfolio/2/transactions?currency=jpy&limit=100&type=ALL"

        # portfolio rate Get请求
        self.portfolio_rate = "https://proj.gtomato.com.cn/mobile/v1/portfolio/4/xrate"

        # portfolio holdings Get请求
        self.portfolio_holdings = "https://proj.gtomato.com.cn/mobile/v1/portfolio/2/holdings?currency=USD"

        # portfolio allocation holdings Get请求
        self.portfolio_allocation_holdings = "https://proj.gtomato.com.cn/mobile/v1/portfolio/1/holdings/allocation?category=Asset&categoryId=1_1&currency=jpy"

        # portfolio allocation holding group Get请求
        self.portfolio_allocation_holding_group = "https://proj.gtomato.com.cn/mobile/v1/portfolio/1/holdings/allocation/group?category=asset&categoryId=1_1&currency=GBP"

        # portfolio liability list Get请求
        self.portfolio_liability_list = "https://proj.gtomato.com.cn/mobile/v1/portfolio/1/liabilities?currency=jpy"

        # portfolio liability detail Get请求
        self.portfolio_liability_detail = "https://proj.gtomato.com.cn/mobile/v1/liabilities/1/detail?currency=jpy"

        # holding detail Get请求
        self.holding_detail = "https://proj.gtomato.com.cn/mobile/v1/holdings/3/detail?holdingid=1&currency=JPY"





        # version control Get请求
        self.version_control = "https://proj.gtomato.com.cn/mobile/v1/version"

        # logout Get请求
        self.logout = "https://proj.gtomato.com.cn/mobile/v1/logout"



    def tearDown(self):
        print("")

    def test_search_customer_userprofilel(self):

        dict_headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": r"application/json;charset=UTF-8"}
        """所有参数为空添加"""
        payload = {"eid": "", "name": "", "limit2": "", "address": "", "start_time": ""}

        r = requests.get(self.base_url, headers=dict_headers)
        # r = requests.get(self.base_url, headers=dict_headers, verify=False)
        self.result = r.json()
        self.assertEqual(self.result["code"], "0")
        self.assertEqual(self.result["message"], "success")
        print('code: '+self.result["code"])
        print('message: '+self.result["message"])
        print(self.result)


        print("customer userprofile hedaers:\n"+str(r.headers))
        print("customer userprofile hedaers-->AMSESSION:  "+r.headers.get("AMSESSION"))
        print("customer userprofile hedaers-->LtpaToken2:  "+r.headers.get("LtpaToken2"))
        # print()
        headers["AMSESSION"] = r.headers.get("AMSESSION")
        headers["LtpaToken2"] = r.headers.get("LtpaToken2")
        headers["Content-Type"] = "application/json;charset=UTF-8"

        print("headers is:  "+str(headers))


    def test_search_customer_userprofilel1(self):

        r = requests.get(self.customer_overview, headers=headers)
        # r = requests.get(self.base_url, headers=dict_headers, verify=False)
        self.result1 = r.json()
        # self.assertEqual(self.result["data"], "Jones")
        # self.assertEqual(self.result["data.customer.netAssetsCurrency"], "GBP")
        print("*******************************")
        print(self.result1["data"])
        print(self.result1["data"]["customer"]["name"])

        # print('netAssetsCurrency: '+self.result["data.customer.netAssetsCurrency"])
        print("customer overview call result: "+str(self.result1))




    def test_search_customer_userprofilel2(self):

        # -- r.status_code  # 响应状态码
        # -- r.content  # 字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
        # -- r.headers  # 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
        # -- r.json()  # Requests中内置的JSON解码器
        # -- r.url  # 获取url
        # -- r.encoding  # 编码格式
        # -- r.cookies  # 获取cookie
        # -- r.raw  # 返回原始响应体
        # -- r.text  # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
        # -- r.raise_for_status()  # 失败请求(非200响应)抛出异常

        body= {"docType":"All", "accountIds":[], "categories":[]}
        r = requests.post(self.customer_documents, json=body, headers=headers)
        print("url is:  " + r.url)

        # print("cookies is:  " + r.cookies)
        print("encoding is:  " + r.encoding)
        # print("原始响应体： " + r.raw)
        print("字节方式的响应体：  " + str(r.content))
        print(r.content)

        self.result2 = r.json()
        print("body is:  " + r.text)
        print("customer documents call result: " + str(self.result2))
        print(self.result2["data"]["documentsGroup"][0]["date"])
        print(self.result2["data"]["documentsGroup"][0]["documents"])
        print(self.result2["data"]["documentsGroup"][0]["documents"][0]["accountName"])
        self.assertEquals(self.result2["data"]["documentsGroup"][0]["documents"][0]["accountName"], "Mr & Mrs Jones")



    # def test_add_event_eid_exist(self):
    #     """id已经存在"""
    #     payload = {"eid": 1, "name": "一加4发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018-11-01 08:00:00"}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], 10022)
    #     self.assertEqual(self.result["message"], "event id already exists")
    #
    # def test_add_event_name_exists(self):
    #     """名称已经存在"""
    #     payload = {"eid": 88, "name": "红米Pro发布会", "limit2": 2000, "address": "深圳宝体",
    #                "start_time": "2018-11-01 08:00:00"}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], 10023)
    #     self.assertEqual(self.result["message"], "event name already exists")
    #
    # def test_add_event_data_type_error(self):
    #     """日期格式错误"""
    #     payload = {"eid": 102, "name": "一加4发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018"}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"], 10024)
    #
    # def test_add_event_success(self):
    #     """添加成功"""
    #     payload = {"eid": 88, "name": "孙小二发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018-11-01 08:00:00"}
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     print(self.result)
    #     self.assertEqual(self.result["status"], 200)


if __name__ == '__main__':
    # test_data.init_data()  # 初始化接口测试数据


    print("*********************")
    # print("*********************")
    # unittest.main()
