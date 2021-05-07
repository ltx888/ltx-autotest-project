#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司

# 1.编写mtx商城的登录
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #这个类里边是专门用来处理web等待


# 1.实例化
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 2.进入首页
driver.get('http://121.42.15.146:9090/mtx/')
#这里发现,主页上有两个"登录"按钮可以跳转到logininfo(登陆输入页面).
# 这种情况,可以理解为.首页有两种跳转到登录的方式.在case层可以分别设置检查.
# 这个case的终点就是跳转到登录页面(和登录各种输入都没有关系).
xpath = "//div[@class='menu-hd']//a[text()='登录']"
# 3.跳转到"登录页面"
driver.find_element_by_xpath(xpath).click()
sleep(2)

xpath = "//input[@placeholder='用户名/手机/邮箱']"#用户名输入框
driver.find_element_by_xpath(xpath).send_keys('bull')
sleep(2)

xpath = "//input[@placeholder='登录密码']"  #密码输入框
driver.find_element_by_xpath(xpath).send_keys('123456')
sleep(2)

xpath = "//div[@class='am-form-group am-form-group-refreshing']/button" #确认登录按钮
driver.find_element_by_xpath(xpath).click()
