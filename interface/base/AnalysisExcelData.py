#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import openpyxl
import datetime
import time

# year_list = [2013, 2014, 2015, 2016, 2017, 2018]
# year_list = ['图文', '图集', '视频', 'Vlog']
year_list = [1, 2, 3, 8]
file_path = r"F:/sql"
file_name = "newsList.xlsx"
file_result = os.path.join(file_path, file_name)


def excel():
    """
    """
    wb = openpyxl.load_workbook(file_result)
    sh = wb.active
    index = 0
    for i in range(len(year_list)):
        count = 2
        sh1 = wb.create_sheet(str(year_list[index]))

        for rows in sh.rows:
            # if rows[0].coordinate != "A1" and datetime.datetime.strptime(rows[0].value, '%Y-%m-%d %H:%M:%S %Z').year == year_list[index]:
            if rows[0].coordinate != "A1" and rows[4].value == year_list[index]:
                # print(rows[0].value, rows[1].value)
                sh1["A1"] = "id"
                sh1["B1"] = "title"
                sh1["C1"] = "news_type"
                sh1["A" + str(count)] = rows[0].value
                sh1["B" + str(count)] = rows[1].value
                sh1["C" + str(count)] = rows[4].value

                # print("in sh:", sh1["A" + str(count)].value, sh1["B" + str(count)].value)
                # print(f"正在分析{year_list[index]}年数据.....")
                print(f"正在分析{year_list[index]}类型数据.....")
                count += 1
        index += 1
    wb.save("newsList.xlsx")

if __name__ == "__main__":
    start_time = time.time()
    excel()
    print(f"分析完成，用时时间为{time.time() - start_time}秒")