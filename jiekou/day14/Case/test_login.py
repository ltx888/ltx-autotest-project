#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
import yaml
import pytest
from selenium import webdriver
import threading
from tomorrow import threads
# 描述
# 1.case的首要目标是,设计检查点
# 2.case层是按照真实测试步骤,串联业务操作的层


#这个case,实现正向登录测试用例
import os
from  tomorrow import threads
from day14.setting import DIR_NAME
from day14.Page.index_page import Page_index
from day14.Page.login_page import Page_login

from time import ctime, sleep

# 读取yaml 文件数据
def dushu():
    path = DIR_NAME + '/case/testdata/test_login.yaml'
    f = open(path, 'r', encoding='utf-8')
    data = yaml.safe_load(f)
    return data

class Test_Mtx_login():

    def select_browser(self,browser):
        print("start %s" % browser, ctime())
        try:
            if browser == 'Chrome' or browser == "Ch":
                driver = webdriver.Chrome('/Users/lvtiexin/Documents/server/chromedriver')
            elif browser == 'Firefox' or browser == 'Ff':
                driver = webdriver.Firefox(executable_path='/Users/lvtiexin/Documents/server/geckodriver')
            else:
                print("Not found %s browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘" % browser)
            return driver
        except Exception as msg:
            print("启动浏览器出现异常：%s" % str(msg))


    def login1(self,driver):
        print('*************进入login1方法***********************8')
        driver = self.select_browser(driver)
        driver.implicitly_wait(10)

        obj_index = Page_index(driver)
        # 调用into_LoginPage方法/动作
        obj_index.into_LoginPage(driver)
        obj_login = Page_login()
        #参数化
        list = dushu()['data']
        print(list)
        for a in list:
            print('*************进入dushu方法***********************8')
            print(a)
            username = a[0]
            kw = a[1]
            obj_login.login(driver, username=username, kw=kw)
            # 根据业务顺序,在这里设计一个检查点
            xpath = f"//em[text()='{username}，欢迎来到']"
            #assert driver.find_element_by_xpath(xpath)
            sleep(3)
        driver.quit()


    # def test_login(self):
    #     names = ["Firefox","Chrome"]
    #     for i in names:
    #         self.login1(i)

    def test_thread_browser(self,args=('Firefox','Chrome')):
        if args:
            threads = []  # 创建线程列表
            for browser in args:
                t = threading.Thread(target=self.login1, args=(browser, ))  # 创建线程
                threads.append(t)
            for t in threads:
                t.start()  # 启动线程
            for t in threads:
                t.join()  # 守护线程
            print("end all time %s" % ctime())
        else:
            print("Please pass at least one browser name")


if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])