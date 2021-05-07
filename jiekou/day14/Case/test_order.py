#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 20, 2021
# @Copyright：北京码同学网络科技有限公司

# 这个case里,要写从登陆→买一个小米手机

import pytest
from selenium import webdriver

from day14.Page.buy_index_page import Page_buy_index
from day14.Page.goods_info import Page_goods_info
from day14.Page.goods_page import Page_goods
from day14.Page.index_page import Page_index
from day14.Page.login_page import Page_login


class Test_Mtx_Order():
    def setup_class(self):
        # 新建driver
        # 1.实例化driver对象
        self.driver = webdriver.Chrome('/Users/lvtiexin/Documents/server/chromedriver')
        self.driver.implicitly_wait(10)

    def test_index_login(self):
        obj_index = Page_index(self.driver)
        #可以检查,成功的打开了Mtx商城
        assert self.driver.title =='码同学实战系统'

        obj_index.into_LoginPage(self.driver)
        #登陆账户
        obj_login = Page_login()
        obj_login.login(self.driver, username='bull1', kw='123456')
        # 检查登陆"某账号"成功的欢迎信息
        assert self.driver.find_element_by_xpath("//*[text()='bull1，欢迎来到']")
        #等待页面跳转回首页后,使用鼠标进入商品搜索
        obj_index.mouse_to_goods(self.driver)

    def test_goods(self):
        obj_goods = Page_goods()
        obj_goods.into_goods_info(self.driver)

        obj_goods_info = Page_goods_info()
        obj_goods_info.bug_now(self.driver)


    def test_buy(self):
        obj_buy_index = Page_buy_index()
        obj_buy_index.payment_1(self.driver)

    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv','test_order.py'])