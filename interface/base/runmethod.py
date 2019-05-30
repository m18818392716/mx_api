#-*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:49
# @Author  : Susanna Chen
# @Site    : 
# @File    : runmethod.py
# @Software: PyCharm

import requests

# 解决提示'InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings'
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import json
class RunMethod:
    # 处理application/x-www-form-urlencoded; charset=utf-8的请求
    def post_main(self, url, data, header=None):
        print('请求参数：%s' % data)
        print('请求头：%s' % header)
        res = None
        if header !=None:
            # res = requests.post(url=url, data=data, headers=header, verify=False)
            res = requests.post(url=url, params=data, headers=header, verify=False)
        else:
            # res = requests.post(url=url, data=data, verify=False)
            res = requests.post(url=url, params=data, verify=False)
        # return res.json()

        print('请求url：%s' % res.url)
        # print('请求参数类型：%s' % type(data))
        print('返回状态码：%s' % res.status_code)

        if res.content:
            return res.json()

    def get_main(self, url, data=None, header=None):
        print('请求参数：%s' % data)
        print('请求头：%s' % header)
        res = None
        if header !=None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        # return res.json()

        print('请求url：%s' % res.url)
        # print('请求参数类型：%s' % type(data))
        print('返回状态码：%s' % res.status_code)

        if res.content:
            return res.json()

    def run_main(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)

        responseJson = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        # 返回的数据有点长..
        # print('返回数据：\n%s' % responseJson)
        return responseJson
        # return res



    # 处理application/json的请求
    def post_main_json(self, url, data, header=None):

        print('请求参数：%s' % data)
        print('请求header：%s' % header)
        res = None
        if header !=None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
            # res = requests.post(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
            # res = requests.post(url=url, params=data, verify=False)
        # return res.json()

        print('请求url：%s' % res.url)
        # print('请求参数类型：%s' % type(data))
        print('返回状态码：%s' % res.status_code)

        if res.content:
            return res.json()

    def run_main_json(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main_json(url, data, header)
        else:
            res = self.get_main(url, data, header)

        responseJson = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        # 返回的数据有点长..
        # print('返回数据：\n%s' % responseJson)
        return responseJson
        # return res



    def post_request(self, url, data, header=None):
        res = None
        if header !=None:
            # res = requests.post(url=url, data=data, headers=header, verify=False)
            res = requests.post(url=url, params=data, headers=header, verify=False)
        else:
            # res = requests.post(url=url, data=data, verify=False)
            res = requests.post(url=url, params=data, verify=False)

        if res.content:
            # print('请求url：%s' % res.url)
            return res

    def get_request(self, url, data=None, header=None):
        res = None
        if header !=None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
            # res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
            # res = requests.get(url=url, data=data, verify=False)

        if res.content:
            # print('请求url：%s' % res.url)
            return res

    def run_request(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_request(url, data, header)
        else:
            res = self.get_request(url, data, header)

        return res






    def post_request_json(self, url, data, header=None):
        res = None
        if header !=None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
            # res = requests.post(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
            # res = requests.post(url=url, params=data, verify=False)

        if res.content:
            # print('请求url：%s' % res.url)
            return res

    def run_request_json(self,method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_request_json(url, data, header)
        else:
            res = self.get_request(url, data, header)

        return res