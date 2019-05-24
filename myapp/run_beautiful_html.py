import unittest
import time
from BeautifulReport import BeautifulReport
from myapp.testCase.case1 import case1

# 此py文件运行方式是python

# class Testaa1(unittest.TestCase):
# #
# #     def testCreateFolder(self):
# #         '''
# #
# #         :return:
# #         '''
# #         print('test case one')
# #
# #     def testDeleteFolder(self):
# #         '''
# #
# #         :return:
# #         '''
# #
# #         print('test case two')



if __name__ == '__main__':

    # test_dir = './testCase'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern="case1.py", top_level_dir=None)
    # print(discover)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    suite = unittest.TestSuite()
    # suite.addTests(discover)
    suite.addTests(unittest.makeSuite(case1))  # 这个类里面所有的测试用例

    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    result = BeautifulReport(suite)

    result.report(filename=now+'_report.html', description='测试报告Demo, log_path=''', log_path='test_beautiful_Report/')