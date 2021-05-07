from time import sleep
from  selenium import webdriver
import yaml
from selenium.webdriver import ActionChains

from uijichu.page.BasePage import BasePage

class Page_index(BasePage):
    def __init__(self):
        f = open('/Users/lvtiexin/PycharmProjects/ui/uijichu/data/index_element.yaml','r',encoding='utf-8')
        self.data = yaml.safe_load(f)
        url = self.data['url']
        self.driver = webdriver.Chrome('/Users/lvtiexin/Documents/server/chromedriver')
        self.driver.get(url)

    #调用basepage 里面的base_find_element 这个方法里面有显示等待
    def into_LoginPage(self, driver):
        into_login_button = self.data['into_login_button']
        self.base_find_element(driver, into_login_button).click()
        sleep(2)

    # 首页搜索
    def search_to_goods_index(self, driver,search_txt='手机'):
        id = self.data['search_input']
        # 找到搜索栏
        search_input = driver.find_element_by_id(id)
        # 输入文字
        search_input.send_keys(search_txt)
        id = self.data['search_button']
        # 点击"搜索"按钮
        sleep(2)
        driver.find_element_by_id(id).click()

     # 1.从首页使用左侧碳层进入手机商品页面-首页对象来实现
    def mouse_to_goods(self, driver):
        self.base_wait(2)
        #由于只有全屏页面才能展示出侧边栏 ，所以
        driver.maximize_window()
        # 鼠标悬浮到侧边栏，展开二级菜单
        element_mouse = self.data['element_mouse']
        element = driver.find_element_by_xpath(element_mouse)
        ActionChains(driver).move_to_element(element).perform()
        self.base_wait()
        # 点击一个具体项目-手机
        mouse_phone = self.data['mouse_phone']
        self.base_find_element(driver,mouse_phone).click()

