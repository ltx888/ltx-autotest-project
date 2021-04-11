#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: order_api.py
# @Author: Bull
# ---
import yaml

from day8.api.Base_Req import Base_Req
from day8.api.login_api import login_api
from day8.setting import HEADERS, DIR_NAME


# 如何编写一个接口封装
# 1.新建该接口对应的类*可以继承基础类
# 2.编写请求方法
#     2.1读取数据文件
#     2.2调用request请求
#     2.3处理响应信息


class order_api(Base_Req):


    def order(self, session):
        path =DIR_NAME+'/api/order_api.yaml'
        with open(path, 'r', encoding='utf-8')as f:
            self.data = yaml.safe_load(f)
            self.url = self.data['url']

        data = {
            'goods_id': 1,
            'stock': 2,
            'buy_type': 'goods',
            'address_id': 600,
            'payment_id': 1,
            'spec': '',

        }
        resp_order = session.post(self.url, data=data, headers=HEADERS)
        print(resp_order.json())

        return session, resp_order

#如果想封装一个 登录+下单 的方法,可以吗?
    def login_and_order(self):
        obj_login = login_api()
        session, resp = obj_login.login()

        obj_order = order_api()
        session, resp_order = obj_order.order(session=session)
        return session, resp_order


if __name__ == '__main__':
    #这个案例中,用session来传递登录状态
    # 所以需要先获取,登录成功的session
    obj_login = login_api()
    session,resp = obj_login.login()
    a,b = obj_login.login()


    obj_order = order_api()
    obj_order.order(session=session)