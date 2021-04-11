#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: login_api.py
# @Author: Bull
# ---
import requests
import yaml

from day8.api.Base_Req import Base_Req
from day8.setting import HEADERS, DIR_NAME
from day8.tools.log import Getlog


class login_api(Base_Req):
    def __init__(self):
        path =DIR_NAME+'/api/login_api1.yaml'
        with open(path, 'r', encoding='utf-8')as f:
            self.data = yaml.safe_load(f)
            self.url = self.data['url']
        self.logger = Getlog().get_logger()

    def login(self, session=requests.Session()):#登录成功
        resp_login = session.post(url=self.url, data=self.data['data'], headers=HEADERS)
        print(resp_login.text)
        return session,resp_login

    def login_v(self,username: str,pwd: str,session=requests.Session()):#封装的自定义登录请求,可以用来进行异常情况
        data = {'accounts': username, 'pwd': pwd}
        resp_login = session.post(url=self.url, data=data, headers=HEADERS)
        print(resp_login.text)
        return session, resp_login

if __name__ == '__main__':
    obj = login_api()
    obj.login()

    #这个案例针对一个接口,
    # 我写了一个py文件
    # 一个对应的data.yaml
    # 好处是:yaml文件的内容看起来会比较清晰
    # 缺点:文件的数量会比较多