import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
href = driver.find_element_by_link_text("学术").get_attribute('href')  # 获取百度主页学术的链接
js = 'window.open("{}");'.format(href)  # javaScript语句,通过这条语句在新的标签页打开百度学术
driver.execute_script(js)  # 执行JavaScript语句
baidu_handle = driver.current_window_handle  # #获取百度主页的窗口句柄
handles = driver.window_handles  # 获取浏览器打开的所有标签页的句柄
for handle in handles:
    if handle != baidu_handle:
        xueshu_handle = handle
print(baidu_handle, xueshu_handle)
print('now window handle:', driver.current_window_handle)
driver.switch_to.window(xueshu_handle)  # 切换标签页,原本在百度主页的页面,现在切换到百度学术
print("now window handle:", driver.current_window_handle)
time.sleep(2)
driver.close()  # 关闭当前标签页,close和quit的区别是一个是关闭当前页,一个是关闭浏览器
driver.switch_to.window(baidu_handle)  # 切换到百度主页
time.sleep(2)
driver.close()