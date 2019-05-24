import unittest
from BeautifulReport import BeautifulReport

def calc(x,y):
    return x+y

class TestCalc(unittest.TestCase):
    def test_pass_case(self):
        '''这是成功的用例'''
        #上面一行是注释，显示在测试报告的用例描述列，不能用#注释，只能用‘‘‘
        print('这是一条通过的用例')
        res = calc(1, 2)
        self.assertEquals(3, res)
    def test_fail_case(self):
        '''这是失败的用例'''
        print('这是一条失败的用例')
        res = calc(1, 2)
        self.assertEquals(5, res)

if __name__=='__main__':


    suite = unittest.TestSuite() #定义一个测试套件
    suite.addTests(unittest.makeSuite(TestCalc)) #这个类里面所有的测试用例
    # suite.addTest(TestCalc(‘test_pass_case‘))  #单个添加用例
    result = BeautifulReport(suite)

    result.report(filename='测试报告B.html', description='描述B, log_path=''')  # 默认在当前路径下，可以加log_path