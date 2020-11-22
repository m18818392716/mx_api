'''
选项卡管理：切换选项卡，有js的方式windows.open,有windows快捷键：
ctrl+t等，最通用的就是js的方式
'''

import time
from selenium import webdriver

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')

    # execute_script: 执行javascrpit代码
    # 弹窗操作
    # browser.execute_script('alert("tank")')

    # 新建浏览器窗口
    # browser.execute_script(
    #     '''
    #     window.open();
    #     '''
    # )
    time.sleep(2)

    browser.execute_script("window.open('https://www.douban.com')")
    time.sleep(2)
    print(browser.window_handles)  # 获取所有的选项卡
    # 切换到第二个窗口
    # 新:
    browser.switch_to.window(browser.window_handles[1])
    # 旧:
    # browser.switch_to_window(browser.window_handles[1])

    # 第二个窗口往淘宝发送请求
    browser.get('https://www.taobao.com')
    time.sleep(5)

    # 切换到第一个窗口
    # browser.switch_to_window(browser.window_handles[0])
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://www.sina.com.cn')

    time.sleep(10)
finally:
    browser.close()