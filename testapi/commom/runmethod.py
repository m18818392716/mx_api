#coding:utf-8
import requests
import json
class RunMethod:

    def post_mian(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_mian(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res.json()

    def run_mian(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_mian(url, data, header)
        else:
            res = self.get_mian(url, data, header)
        return json.dumps(res, ensure_ascii=False)

if __name__ == '__main__':
    print('')