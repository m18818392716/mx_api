# -*- coding: utf-8 -*-
# @Author  : leizi
import requests,json
from myapp.Public.log import LOG,logger
@logger('requests封装')
class requ():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}
        # self.headers = {"AMSESSION":"ukdata5", "Region":"uk", "Content-Type": r"application/json;charset=UTF-8"}


    def get(self, url, params, headers):#get消息
        try:
            r = requests.get(url, params=params, headers=headers)
            r.encoding = 'UTF-8'
            # json_response = json.loads(r.text)
            json_response = r.json()
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info('get请求出错，出错原因:%s'%e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s'%e}


    def post(self, url, json, headers):#post消息
        # data = json.dumps(json)
        try:
            r =requests.post(url, json=eval(json), headers=headers)
            # json_response = json.loads(r.text)
            json_response = r.json()
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}



    def delfile(self,url,params):#删除的请求
        try:
            del_word=requests.delete(url,params=params,headers=self.headers)
            json_response=json.loads(del_word.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('del请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}


    def putfile(self,url,params):#put请求
        try:
            data=json.dumps(params)
            me=requests.put(url,data)
            json_response=json.loads(me.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('put请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}