import unittest
import time
from myapp.Public.BSTestRunner import BSTestRunner

test_dir='./testCase'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="case.py")
print(discover)
suite = unittest.TestSuite()
suite.addTests(discover)
# print(suite)



if __name__ == '__main__':

    # start_interface_html_http()

    report_dir ='./test_bstestrunner_Report'
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir +'/'+now +'.html'

    # 使用with打开文件后可以不用close文件
    with open(report_name,'wb')as f:

        runner = unittest.TextTestRunner()
        # runner.run(suite)

        runer = BSTestRunner(stream=f, title="Test Report", description='Test case result')
        runer.run(suite)