#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司

# 基类,是把page对象共用的一些方法抽离出来.复用,减少代码编写难度
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from time import sleep

class BasePage():
    # 显示等待 / js点击 / sleep阻塞N秒

    def base_find_element(self,driver,xpath,timeout=15,pool=0.5):
        return WebDriverWait(driver,timeout, pool).until(lambda e: e.find_element_by_xpath(xpath))

    def js_click(self,driver,xpath):
        return driver.execute_script('arguments[0].click()',self.base_find_element(driver,xpath))

    def base_wait(self,s=5):
        s = int(s)
        time.sleep(s)
