#from selenium import webdriver
#import time
import pytest
# driver = webdriver.Firefox(executable_path='/Users/lvtiexin/Documents/server/geckodriver')
# time.sleep(2)
# driver.get('http://121.42.15.146:9090/mtx/')


from time import ctime, sleep
from selenium import webdriver
import threading


def select_browser(browser):
    print("start %s" % browser, ctime())
    try:
        if browser == 'Chrome' or browser == "Ch":
            dr = webdriver.Chrome('/Users/lvtiexin/Documents/server/chromedriver')
        elif browser == 'Firefox' or browser == 'Ff':
            dr = webdriver.Firefox(executable_path='/Users/lvtiexin/Documents/server/geckodriver')
        else:
            print("Not found %s browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘" % browser)
        return dr
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

def test_baidu(browser_name,username,kw):
    driver = select_browser(browser_name)
    driver.maximize_window()
    driver.get("https://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(username)
    print(kw)
    sleep(2)
    print(driver.title)
    driver.quit()
    print("end %s" % browser_name, ctime())


def thread_browser(*args):
    if args:
        threads = []  # 创建线程列表
        for browser,data in args:
            t = threading.Thread(target=test_baidu, args=(browser,data))  # 创建线程
            threads.append(t)
        for t in threads:
            t.start()  # 启动线程
        for t in threads:
            t.join()  # 守护线程
        print("end all time %s" % ctime())
    else:
        print("Please pass at least one browser name")


if __name__ == "__main__":
    thread_browser('Firefox', ['bull'])


