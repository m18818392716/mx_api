from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

url = 'https://baidu.com'

def press_login():
    # login = driver.find_element_by_name("tj_login")
    login = driver.find_element_by_xpath("//*[@id='u1']/a")
    login.click()


def press_login_by_account():
    LoginByAccount = driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn")
    LoginByAccount.click()

def input_username():
    login = driver.find_element_by_name("userName")
    login.send_keys('18818392716')

def input_pwd():
    login = driver.find_element_by_name("password")
    login.send_keys('cq183158')

def press_submit():
    login = driver.find_element_by_id("TANGRAM__PSP_11__submit")
    login.click()


# def press_check_box():
#     driver.find_element_by_xpath("//*[@name='memberPass']").click()


driver.get(url)
print('登录网址：', url)
time.sleep(2)
press_login()
print('成功点击【登录】按钮')
time.sleep(2)
press_login_by_account()
print('成功点击【用户名登录】')
time.sleep(2)
input_username()
print('点击【下次自动登录】')
time.sleep(2)
input_pwd()
print('再次点击【下次自动登录】')
press_submit()
print('脚本完成。')