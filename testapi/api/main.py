from testapi.api.read_excel import test_cases_in_excel
from testapi.api.send_email import send_email


def main():
    # 执行所以测试用例，获取错误的用例
    error_cases = test_cases_in_excel("testcases.xlsx")
    # 如果有错误接口，则开始构造html报告
    if len(error_cases) > 0:
        html = '<html><body>接口自动化扫描，共有 ' + str(len(error_cases)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th></tr>'
        for test in error_cases:
            html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td></tr>'
        send_email(html)
        print(html)
        with open ("report.html", "w") as f:
            f.write(html)
    else:
        print("本次测试，所有用例全部通过")
        send_email("本次测试，所有用例全部通过")