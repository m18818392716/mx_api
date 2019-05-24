# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  : lileilei
from myapp.Public.fengzhuang_dict import res
from .log import LOG,logger
@logger('断言测试结果')
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(res(fanhuijson,key))) for key in result.keys()])
# ['[0]','1']
#         value1=' '.join([(str(res(fanhuijson,key))) for key in result.keys()])
#         value1=' '.join((str(res(fanhuijson,key))) for key in result.keys())
        value2=([(str(value)) for value in result.values()])

        value3=([(str(res(fanhuijson,key))) for key in result.keys()])

        print("expected value: %s" % type(value2))
        print("actualed value: %s" % type(value1))
        print("expected value: %s" % value2)
        print("actualed value: %s" % value1)
        print("actualed value3: %s" % value3)
        print("result:", value1 == value2)
        # print("actualed value valu3 : %s" % value3)

        if value1 == value2:
            return  { 'code':0,"result":'pass'}
        else:
            return {'code':1,'result':'fail'}
    else:
        LOG.info('填写测试预期值')
        return  {"code":2,'result':'填写测试预期值'}
@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        raise {"code":1,'result':'填写测试预期值'}