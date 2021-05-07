
import requests
import yaml
from day88.api.Base_Req1 import Base_Req1
from day88.tools.log1 import logger
from day88.setting1 import DIR_NAME,IP,HEADERS

class login_api1(Base_Req1):
    def __init__(self):
        # 调用父类的构造方法
        Base_Req1.__init__(self)
        # 读取yaml数据
        path = DIR_NAME + '/api/login_api1.yaml'
        f = open(path, 'r' ,encoding='utf-8')
        self.data = yaml.safe_load(f)

    def login1(self):
        # 登陆接口的url以及数据
        self.login_data = self.data['data']
        self.url = self.data['url']
        # 调用父类的post方法模版
        resp_login = self.post_template(url=self.url,data=self.login_data)
        return resp_login

if __name__ == '__main__':
    obj = login_api1()
    obj.login1()

