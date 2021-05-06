#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
import yaml
from time import sleep
from selenium import webdriver
from day14.Page.index_page import Page_index
from day14.setting import DIR_NAME#为了方便调试关联关系而导入


class Page_login():#用来描述"logininfo登录详情页"中的操作


    def login(self,driver,username,kw):
        xpath = "//input[@placeholder='用户名/手机/邮箱']"  # 用户名输入框
        driver.find_element_by_xpath(xpath).send_keys(username)
        sleep(2)

        xpath = "//input[@placeholder='登录密码']"  # 密码输入框
        driver.find_element_by_xpath(xpath).send_keys(kw)
        sleep(2)

        xpath = "//div[@class='am-form-group am-form-group-refreshing']/button"  # 确认登录按钮
        driver.find_element_by_xpath(xpath).click()

if __name__ == '__main__':
    #调试两个页面的关联
    # 1.实例化driver对象
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # 2.实例化page对象
    obj_index = Page_index()
    # 3.调用into_LoginPage方法/动作
    obj_index.into_LoginPage(driver)

    # 4.调用登录页面Page_login,封装的动作login()
    obj_login = Page_login()
    obj_login.login(driver)