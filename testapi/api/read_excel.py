import xlrd
import sys
import os
from testapi.api.interface_test import interface_test

def test_cases_in_excel(test_case_file):
    test_case_file = os.path.join(os.getcwd(), test_case_file)
    # 获取测试用例全路径 如：E:\Python\httprunner\interface_excel\testcases.xlsx
    print(test_case_file)
    if not os.path.exists(test_case_file):
        print("测试用例excel文件存在或路径有误！")
        # 找不到指定测试文件，就退出程序 os.system("exit")是用来退出cmd的
        sys.exit()
    # 读取excel文件
    test_case = xlrd.open_workbook(test_case_file)
    # 获取第一个sheet，下标从0开始
    table = test_case.sheet_by_index(0)
    # 记录错误用例
    error_cases = []
    # 一张表格读取下来，其实就像个二维数组，无非是读取第一行的第几列的值，由于下标是从0开始，第一行是标题，所以从第二行开始读取数据
    for i in range(1, table.nrows):
        num = str(int(table.cell(i, 0).value)).replace("\n", "").replace("\r", "")
        api_name = table.cell(i, 1).value.replace("\n", "").replace("\r", "")
        api_host = table.cell(i, 2).value.replace("\n", "").replace("\r", "")
        request_url = table.cell(i, 3).value.replace("\n", "").replace("\r", "")
        method = table.cell(i, 4).value.replace("\n", "").replace("\r", "")
        request_data_type = table.cell(i, 5).value.replace("\n", "").replace("\r", "")
        request_data = table.cell(i, 6).value.replace("\n", "").replace("\r", "")
        check_point = table.cell(i, 7).value.replace("\n", "").replace("\r", "")
        print(num, api_name, api_host, request_url, method, request_data_type, request_data, check_point)
        try:
            # 调用接口请求方法，后面会讲到
            status, resp = interface_test(num, api_name, api_host, request_url, method,
                                            request_data_type, request_data, check_point)
            if status != 200 or check_point not in resp:
                # append只接收一个参数，所以要讲四个参数括在一起，当一个参数来传递
                # 请求失败，则向error_cases中增加一条记录
                error_cases.append((num + " " + api_name, str(status), api_host + request_url))
        except Exception as e:
            print(e)
            print("第{}个接口请求失败，请检查接口是否异常。".format(num))
            # 访问异常，也向error_cases中增加一条记录
            error_cases.append((num + " " + api_name, "请求失败", api_host + request_url))
    return error_cases