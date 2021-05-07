import requests
import yaml
from day88.api.Base_Req1 import Base_Req1
from day88.setting1 import HEADERS, DIR_NAME,IP
from day88.tools.log1 import Getlog,logger
import pytest

# 订单接口
class order_api1(Base_Req1):


    def __init__(self):
        Base_Req1.__init__(self)
        path = DIR_NAME + '/api/order_api1.yaml'
        f = open(path, 'r',encoding='utf-8')
        self.data = yaml.safe_load(f)

    # 登陆
    def login(self):
        url = self.data['login_url']
        login_data = self.data['login_data']
        resp = self.post_template(url=url,data=login_data)
        print(resp.text)

    # 加入购物车
    def cart(self):
        #加入购物车的url 以及 参数
        cart_url = self.data['cart_url']
        cart_data = self.data['cart_data']
        #响应数据
        resp = self.post_template(cart_data,cart_url)
        print(resp.text)

    def order(self):
        # 提交订单的url 以及 参数
        order_url = self.data['order_url']
        order_data = self.data['order_data']
        # 响应数据
        resp = self.post_template(order_url,order_data)
        resp_dict = resp.json()
        order_id = resp_dict['data']['order']['id']
        payment_id = resp_dict['data']['order']['payment_id']
        return order_id

    def cancle_order(self,order_id):
        cancelorder_url = self.data['cancelorder_url']
        resp = self.post_template(cancelorder_url,order_id)
        return resp



if __name__ == '__main__':
    obj = order_api1()

    obj.login()

    order_id = obj.order()
    print(order_id)
    resp = obj.cancle_order(order_id=order_id)
    print(resp.text)




