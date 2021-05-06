#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司

#这个类里边,主要描述首页的各种可能的操作(定义成一个page类的函数)
from time import sleep
from selenium import webdriver
import yaml
from selenium.webdriver import ActionChains

from day14.Page.BasePage import BasePage


class Page_index(BasePage):
    def __init__(self,driver):
        f = open('/Users/lvtiexin/PycharmProjects/jiekou/day14/Data/index_elements.yaml', 'r', encoding='utf-8')
        self.data = yaml.safe_load(f)
        print(f'读取到的数据格式是:{type(self.data)},\n读取到的值是:{self.data}')
        url = self.data['url']
        # 打开商城首页
        driver.get(url)

    def into_LoginPage(self,driver):
        into_login_button = self.data['into_login_button']
        self.base_find_element(driver,into_login_button).click()
        sleep(2)

    def search_to_goods_index(self,driver,search_text='手机'):
        id = self.data['search_input']
        # 1.找到搜索栏
        search_input = driver.find_element_by_id(id)
        # 2.输入文字
        search_input.send_keys(search_text)
        id = self.data['search_button']
        # 3.点击"搜索"按钮
        sleep(2)
        driver.find_element_by_id(id).click()

# 1.从首页使用左侧弹层进入手机商品页面-首页对象来实现
    def mouse_to_goods(self,driver):
        self.base_wait(2)
        # 由于只有全屏页面才能展示出侧边栏,所以
        driver.maximize_window()
        # 鼠标悬浮到侧边栏,展开二级菜单
        element_mouse = self.data['element_mouse']
        element = driver.find_element_by_xpath(element_mouse)
        ActionChains(driver).move_to_element(element).perform()
        self.base_wait()
        # 点击一个具体项目-手机
        mouse_phone = self.data['mouse_phone']
        self.base_find_element(driver,mouse_phone).click()

if __name__ == '__main__':
    # 1.实例化driver对象
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # 2.实例化page对象
    obj = Page_index()
    # 3.调用into_LoginPage方法/动作
    # obj.into_LoginPage(driver)

    # 3-2,调用search_to_goods_index()方法
    # obj.search_to_goods_index(driver)

    # 这里,我有了一个新的想法.page的编写中,有以下共性的代码:
    #     比如说显示等待/js点击/sleep阻塞N秒
    # 这里就可以把有共性的代码,封装到 页面对象-基础类(也就是"基类/BasePage/BaseClass")

    # 3-3,调用mouse_to_goods()
    obj.mouse_to_goods(driver)