#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
from day14.Page.BasePage import BasePage
from selenium import webdriver

class Page_goods_info(BasePage):
    def bug_now(self,driver):
        driver.switch_to.window(driver.window_handles[-1])
        self.base_wait(2)
        driver.find_element_by_xpath("//*[text()='立即购买']").click()

        # self.js_click(driver,"//button[text()='立即购买']")

