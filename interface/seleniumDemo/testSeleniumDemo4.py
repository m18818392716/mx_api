from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.implicitly_wait(10)
    driver.get('https://www.jd.com/')
    driver.get('https://www.baidu.com/')
    driver.get('https://www.cnblogs.com/')

    time.sleep(2)

    # 回退操作
    driver.back()
    print(driver.current_url)
    print(driver.title)
    time.sleep(1)
    # 前进操作
    driver.forward()
    print(driver.current_url)
    print(driver.title)
    time.sleep(1)
    driver.back()
    print(driver.current_url)
    print(driver.title)
    time.sleep(10)

finally:
    driver.close()