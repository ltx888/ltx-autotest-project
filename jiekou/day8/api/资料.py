 #!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 资料.py
# @Author: Bull
# ---
import requests
from requests import Session

from day8.setting import HEADERS
# from day8.tools.log import logger

# 我们写接口测试之前,用requests调试接口
from day8.tools.log import Getlog


class Case():
    def __init__(self):
        self.logger = Getlog().get_logger()
    def login(self, session=requests.Session()):
        self.url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'
        data = {'accounts': 'bull', 'pwd': '123456'}
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        # self.logger = logger
        self.logger.info('进行登录')

        print(resp_login.json())
        return session,resp_login

    def order(self,session):
        self.url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/buy/add.html'
        data = {
            'goods_id': 1,
            'stock': 2,
            'buy_type': 'goods',
            'address_id': 600,
            'payment_id': 1,
            'spec': '',

        }
        resp_order = session.post(self.url,data=data, headers=HEADERS)
        print(resp_order.json())
        # # 提取数据做数据关联
        # order_id = resp_order.json().get('data').get('order').get('id')
        # setting.ORDER_ID = order_id
        # user_id = resp_order.json().get('data').get('order').get('user_id')
        # setting.USER_ID = user_id
        # payment_id = resp_order.json().get('data').get('order').get('payment_id')
        # setting.PAYMENT_ID = payment_id
        return session,resp_order


    def admin_login(self,session):
        self.url = 'http://121.42.15.146:9090/mtx/admin.php?s=/admin/login.html'
        data = {
            'username': 'shamo',
            'login_pwd': 123456,
        }
        resp_admin_login = session.post(self.url, data=data, headers=HEADERS)
        print(resp_admin_login.json())
        return session,resp_admin_login



    def pay_order(self,session,order_id,payment_id):
        self.url = 'http://121.42.15.146:9090/mtx/admin.php?s=/order/pay.html'
        data = {
            'id': order_id,
            'payment_id': payment_id
        }
        resp_payment = session.post(self.url, data=data, headers=HEADERS)
        print(resp_payment.json())
        return session,resp_payment

if __name__ == '__main__':
    v = Case()
    s1,resp = v.login()
    s1,resp = v.order(s1)
    resp = resp.json()
    order_id = resp['data']['order']['id']
    payment_id = resp['data']['order']['payment_id']
    print(order_id,payment_id)
    s1,resp = v.admin_login(s1)
    s1,resp = v.pay_order(session=s1,order_id=order_id,payment_id=payment_id)