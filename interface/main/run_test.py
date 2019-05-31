# -*- coding:utf-8 -*-
# @Time    : 2019/3/27 下午3:50
# @Author  : Susanna Chen
# @Site    : 
# @File    : run_test.py
# @Software: PyCharm

import sys
import traceback

sys.path.append("D:\software\PycharmProject\APITest\interface")
from interface.tools.case_util import *


class RunTest:
    def __init__(self):
        self.data = GetData()

    # 程序执行的
    def go_on_run(self):
        pass_count = []
        fail_count = []
        # 10  0,1,2,3
        rows_count = self.data.get_case_lines()
        print('rows_count: %d' % rows_count)
        for row in range(1, rows_count):
            print("--------- TEST CASE [ %s ] START ---------" % row)
            try:
                is_run = self.data.get_is_run(row)
                if is_run:
                    run_case_by_row_num(row)
                    self.data.write_result(row, 'pass')
                    pass_count.append(row)
            except Exception:
                print('TEST CASE [ %s ] failed...' % row)
                traceback.print_exc()
                fail_count.append(row)
                self.data.write_result(row, 'failed')
            finally:
                print("--------- TEST CASE [ %s ] END ---------\n" % row)

        print("fail test case: %s" % fail_count)
        print("pass test case: %s" % pass_count)

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
