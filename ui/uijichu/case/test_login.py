#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司
import pytest
from selenium import webdriver
# 描述
# 1.case的首要目标是,设计检查点
# 2.case层是按照真实测试步骤,串联业务操作的层


#这个case,实现正向登录测试用例
from uijichu.page.index_page import Page_index
from uijichu.page.login_page import Page_login


class Test_Mtx_login():
    def setup_class(self):
        # 新建driver
        # 1.实例化driver对象
        self.driver = webdriver.Chrome('/Users/lvtiexin/Documents/server/chromedriver')
        self.driver.implicitly_wait(10)


    def test_index(self):
        # 实例化page对象
        obj_index = Page_index()
        # 调用into_LoginPage方法/动作
        obj_index.into_LoginPage(self.driver)


    @pytest.mark.parametrize('user_name,kw',
                             [['','123456'],
                              ['bull','123456'],
                              ['bull','']
                              ])
    def test_login(self,user_name,kw):
        # username = 'bull'
        # kw = '123456'
        username = user_name
        kw = kw
        # 4.调用登录页面Page_login,封装的动作login()
        obj_login = Page_login()
        obj_login.login(self.driver,username=username,kw=kw)
        # 根据业务顺序,在这里设计一个检查点
        xpath = f"//em[text()='{username}，欢迎来到']"
        assert self.driver.find_element_by_xpath(xpath)


    def teardown_class(self):
        self.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv','--html=report.html','--self-contained-html'])
