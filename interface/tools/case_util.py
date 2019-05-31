from interface.operation_data.get_data import GetData
from interface.base.runmethod import RunMethod
from interface.dataconfig.request_config import *
from interface.case.case_response import *
from interface.tools.operation_excel import OperationExcel
from ptest.assertion import *
import json

excel_data = GetData()
run_method = RunMethod()
opera_excel = OperationExcel()


def run_case_by_row_num(row_num):
    case_id = excel_data.get_case_id(row_num)
    url = excel_data.get_request_url(row_num)
    method = excel_data.get_request_method(row_num)
    content_type = excel_data.get_request_content_type(row_num)
    request_data = excel_data.get_data_for_json(row_num)
    header = excel_data.is_header(row_num)
    depend_case = excel_data.is_depend(row_num)
    if depend_case:
        # 获取的依赖响应数据
        depend_response_data = get_depend_data_by_row(row_num)
        depend_key = excel_data.get_depend_field(row_num).split(',')
        print('依赖关键字：%s' % depend_key)
        print('请求数据：%s' % request_data)
        print('请求数据类型：%s' % type(request_data))

        # 将Excel中定义的请求参数与依赖参数进行合并
        if content_type:
            # 如果不是application/json，那么就拼接字符串的形式： action=1&channel_id=84
            for j, v in enumerate(depend_key):
                if request_data:
                    request_data = '%s&%s=%s' % (request_data, v, depend_response_data[j])
                else:
                    request_data = '%s=%s' % (v, depend_response_data[j])
        else:
            request_data1 = {}
            if request_data:
                request_data1 = json.loads(request_data)

            if method == 'Post':
                # 字符串字典的形式： {'action':1,'channel_id':82}
                for j, v in enumerate(depend_key):
                    request_data1[v] = depend_response_data[j]
                request_data = json.dumps(request_data1)
            else:
                for j, v in enumerate(depend_key):
                    request_data1[v] = depend_response_data[j]
                request_data = request_data1

    response_data = run_request(method, url, request_data, header, content_type)
    assert_equals(response_data['state'], 1, "测试失败...")
    # 保存响应结果
    set_response(case_id, response_data)
    return response_data


# 根据case_row去获取对应依赖的case的响应,然后返回
def get_depend_data_by_row(row):
    case_id = excel_data.get_case_id(row)
    case_name = excel_data.get_case_name(row)
    depend_case_id = excel_data.is_depend(row)
    depend_data = excel_data.get_depend_key(row)

    print('%s %s 依赖数据：%s %s' % (case_id, case_name, depend_case_id, depend_data))

    # 如果已保存过dependent的数据，直接获取
    if get_response(depend_case_id):
        response_data = get_response(depend_case_id)
    else:
        depend_row = opera_excel.get_row_num(depend_case_id)
        response_data = run_case_by_row_num(depend_row)

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


# 执行请求
def run_request(method, url, request_data, header, content_type):
    response_data = None
    if header == 'write':
        # 获取全局header作为请求header，并且保存uuid和token为全局header
        response_data = run_method.run_main(method, url, request_data, get_header())

        uuid = json.loads(response_data)['result']['uuid']
        token = json.loads(response_data)['result']['token']
        set_header('uuid', uuid)
        set_header('token', token)

    elif header == 'yes':
        # 获取全局header
        if content_type:
            new_headers = get_header()
            # 默认content-type为application/json，当不为默认时，暂时视为application/x-www-form-urlencoded
            new_headers['content-type'] = content_type
            response_data = run_method.run_main(method, url, request_data, new_headers)
        else:
            response_data = run_method.run_main_json(method, url, request_data, get_header())

    else:
        response_data = run_method.run_main(method, url, request_data)

    return json.loads(response_data)
