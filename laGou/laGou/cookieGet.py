import json
import time
from selenium import webdriver

class getCookie(object):
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.maximize_window()
    driver.get('https://www.lagou.com/wn/jobs?')
    time.sleep(20)
    # 获取cookies
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)
    with open('cookies.json','w')as f:
         f.write(jsonCookies)
    driver.quit()