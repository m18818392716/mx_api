# -*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:50
# @Author  : Susanna Chen
# @Site    : 
# @File    : dependent_data.py
# @Software: PyCharm

import sys
import json

sys.path.append('/Users/gzuser/PycharmProjects/DemoTest1/interface')
from interface.tools.operation_excel import OperationExcel
from interface.base.runmethod import RunMethod
from interface.operation_data.get_data import GetData
from jsonpath_rw import jsonpath, parse

from interface.tools.operation_header import OperationHeader
from interface.tools.operation_json import OperetionJson
from interface.dataconfig.request_config import *
from interface.case.case_response import *
from interface.tools.case_util import *


class DependentData:

    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

        self.run_method = RunMethod()
        # self.headers = {"AMSESSION": "ukdata5", "Region": "uk", "Content-Type": "application/json;charset=UTF-8"}

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试，获取结果
    def run_dependent(self, case_id):

        # run_method = RunMethod()
        print('依赖case: %s' % case_id)
        row_num = self.opera_excel.get_row_num(case_id)
        print('行数: %s' % row_num)

        request_data = {}
        if (self.data.get_data_for_json(row_num) is not None):
            request_data = self.data.get_data_for_json(row_num)

        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        content_type = self.data.get_request_content_type(row_num)
        case_depend = self.data.is_depend(row_num)
        print('yilaicase: %s' % case_depend)

        data_depend = self.data.get_depend_key(row_num)
        field_depend = self.data.get_depend_field(row_num)

        depend_row_num = self.opera_excel.get_row_num(case_depend)

        if case_depend != None:
            self.depend_data = DependentData(case_depend)
            # 获取的依赖响应数据
            # depend_response_data = self.depend_data.get_data_for_key(depend_row_num)
            depend_response_data = self.depend_data.get_data_for_key(row_num)
            # 获取依赖的key
            # depend_key = self.data.get_depend_field(depend_row_num)
            # depend_key = self.data.get_depend_field(row_num)
            depend_key = self.data.get_depend_field(row_num).split(',')

            # request_data[depend_key] = depend_response_data
            for i, v in enumerate(depend_key):
                request_data[v] = depend_response_data[i]

        return run_request(method, url, request_data, header, content_type)

    # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row):
        case_id = self.data.get_case_id(row)
        case_name = self.data.get_case_name(row)
        depend_case_id = self.data.is_depend(row)
        depend_data = self.data.get_depend_key(row)

        request_data = self.data.get_data_for_json(row)
        header = self.data.is_header(row)
        method = self.data.get_request_method(row)
        url = self.data.get_request_url(row)

        print('%s %s 依赖数据：%s %s' % (case_id, case_name, depend_case_id, depend_data))

        # 如果已保存过dependent的数据，直接获取
        # if get_response(depend_case_id):
        #     response_data = get_response(depend_case_id)
        # else:
        #     # response_data = self.run_dependent(depend_case_id)
        #     response_data = self.run_dependent(depend_case_id)
        response_data = run_case_by_row_num(row)

        str_data = depend_data.split(',')
        list_value = []

        for k in str_data:
            depend_response_key_data = response_data

            key = k.split('.')

            for i in key:

                key_name = i
                index = None
                if i.find('[') > 0:
                    start = i.find('[')
                    key_name = i[0: start]
                    end = i.find(']')
                    index = i[(start + 1): end]

                if isinstance(depend_response_key_data, list):
                    # 如果拿到的数据是集合，那么获取所有object对应的key的值集合
                    depend_list = []
                    for sub_depend_data in depend_response_key_data:
                        depend_list.append(sub_depend_data[key_name])
                    depend_response_key_data = depend_list
                else:
                    depend_response_key_data = depend_response_key_data[key_name]
                    # 如果包含'[]'索引符，则获取索引对应的元素；否则获取整个集合
                    if index:
                        depend_response_key_data = depend_response_key_data[int(index)]

            # return depend_response_key_data
            # print("已获取：[%s : %s]" % (k,depend_response_key_data))
            list_value.append(depend_response_key_data)

        return list_value

        # json_exe = parse(depend_data)
        # madle = json_exe.find(response_data)

        # return [math.value for math in madle][0]

        # list = []  ## 空列表
        # for math in madle:
        #     list.append(math.value)  ## 使用 append() 添加元素
        # return list


if __name__ == '__main__':
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "京东订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=京东订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=京东订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "京东订单-1710141907182334",
            "total_fee": 299
        },
        "errorCode": 1000,
        "errorDesc": "成功",
        "status": 1,
        "timestamp": 1507979239100
    }

    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
