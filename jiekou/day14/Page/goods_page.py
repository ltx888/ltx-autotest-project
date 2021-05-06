#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
from selenium import webdriver

from day14.Page.BasePage import BasePage
from day14.Page.index_page import Page_index


class Page_goods(BasePage):
    def into_goods_info(self,driver):
        self.base_wait(3)
        xpath = "//ul[@class='am-avg-sm-2 am-avg-md-3 am-avg-lg-5 search-list']//li"
        goods_list = driver.find_elements_by_xpath(xpath)
        goods_list[-1].click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    obj = Page_index(driver)
    obj.mouse_to_goods(driver)

    obj_goods = Page_goods()
    obj_goods.into_goods_info(driver)


