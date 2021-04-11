import requests
import yaml
from day88.api.Base_Req1 import Base_Req1
from day88.setting1 import HEADERS, DIR_NAME
from day88.tools.log1 import Getlog
import pytest

# 订单接口
class order_api1(Base_Req1):


    def __init__(self):
        Base_Req1.__init__(self)
        path = DIR_NAME + '/api/order_api1.yaml'
        f = open(path, 'r',encoding='utf-8')
        self.data = yaml.safe_load(f)
        self.logger = Getlog().get_logger()
        self.HEADERS = HEADERS
        self.obj = Base_Req1()

    # 登陆
    def login(self):
        login_url = self.data['login_url']
        print(f'login的url为{login_url}')
        print('*****************************')
        login_data = self.data['login_data']
        resp = obj.post_template(login_data,login_url)
        print(resp.text)

    # 加入购物车
    def cart(self):
        #加入购物车的url 以及 参数
        cart_url = self.data['cart_url']
        cart_data = self.data['cart_data']

        #响应数据
        resp = obj.post_template(cart_data,cart_url)
        print(resp.text)

    def order(self):

        # 提交订单的url 以及 参数
        order_url = self.data['order_url']
        order_data = self.data['order_data']

        #响应数据
        resp = obj.post_template(order_data, order_url)


    def order(self):
        # 提交订单的url 以及 参数
        order_url = self.data['order_url']
        order_data = self.data['order_data']

        # 响应数据
        resp = obj.post_template(order_data, order_url)
        resp_dict = resp.json()

        order_id = resp_dict['data']['order']['id']
        payment_id = resp_dict['data']['order']['payment_id']
        print('%%%%%%%%%%%%%%%%%%%%%%%……¥%^-^6¥%')
        print(order_id, payment_id)
        print(resp.text)





if __name__ == '__main__':
    obj = order_api1()
    obj.login()
    obj.login()
    obj.order()



