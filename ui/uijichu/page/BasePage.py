#基类，是把page对象公用的一些方法抽离出来，复用，减少代码编写难度
import time

from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium import webdriver

class BasePage():
    # 显示等待 / js点击 / sleep阻塞
    def base_find_element(self,driver,xpath,timeout=15,pool=0.5):
        return  WebDriverWait(driver,timeout, pool).util(lambda e: e.find_element_by_xpath(xpath))

    def js_click(self ,driver, xpath):
        return driver.execute_script('arguments[0].click', self.base_find_element(driver, xpath))

    def base_wait(self, s=5):
        s = int(s)
        time.sleep(s)