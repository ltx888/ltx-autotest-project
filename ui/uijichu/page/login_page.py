from time import sleep
from selenium import webdriver

class Page_login():
    def login(self,driver,username,kw):
        xpath = "//input[@placeholder='用户名/手机/邮箱']"  # 用户名输入框
        driver.find_elenment_by_xpath().sendkeys(username)
        sleep(2)


        xpath = "//input[@placeholder='登录密码']"  # 用户名输入框
        driver.find_elenment_by_xpath().sendkeys(kw)
        sleep(2)

        xpath = "//div[@class='am-form-group am-form-group-refreshing']/button"  # 确认登录按钮
        driver.find_element_by_xpath(xpath).click()