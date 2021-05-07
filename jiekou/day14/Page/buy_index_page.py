#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
from selenium import webdriver

from day14.Page.BasePage import BasePage
from day14.Page.goods_info import Page_goods_info
from day14.Page.goods_page import Page_goods
from day14.Page.index_page import Page_index
from day14.Page.login_page import Page_login


class Page_buy_index(BasePage):
    def payment_1(self,driver):
        self.base_wait(3)
        driver.find_element_by_xpath("//*[@class='payment-list']//*[@data-value=1]").click()
        driver.find_element_by_xpath("图片文件的地址")
        self.base_find_element(driver,"//*[@title='点击此按钮，提交订单']").click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    obj_index = Page_index(driver)
    obj_index.into_LoginPage(driver)

    obj_login = Page_login()
    obj_login.login(driver,username='bull1',kw='123456')

    obj_index.mouse_to_goods(driver)

    obj_goods = Page_goods()
    obj_goods.into_goods_info(driver)

    obj_goods_info = Page_goods_info()
    obj_goods_info.bug_now(driver)

    obj_buy_index = Page_buy_index()
    obj_buy_index.payment_1(driver)

