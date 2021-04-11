#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: Base_Req1.py
# @Author: Bull
# ---
# 封装base（基础类、基类）
# 针对MTX商城接口，它的头信息、请求方式、请求方法、ip都可以通用
import requests
# from day8.tools.log import logger
from day8.tools.log import Getlog, logger


class Base_Req(object):
    def __init__(self):
        self.logger = logger
        # self.logger = Getlog().get_logger()#非单例模式调用
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}
        self.logger.info('实例化请求基础类')

    def post_template(self,url,data,session=requests.session()):
        url = self.ip + url
        resp = session.post(url=url,data=data,headers=self.headers)
        self.logger.info(f'请求成功：{resp.text}')
        return resp

if __name__ == '__main__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = {'accounts':'bull','pwd':'123456'}
    req = Base_Req()
    res = req.post_trmplate()
    print(res.json())