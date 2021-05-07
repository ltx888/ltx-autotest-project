import pytest
import html
from day88.api.order_api1 import order_api1
import allure



class Test_order:

    def test_case1(self):
        obj = order_api1()
        obj.login()
        order_id = obj.order()
        resp = obj.cancle_order(order_id=order_id)
        print(resp.text)
        resp = resp.json()
        msg = resp['msg']
        print(msg)

if __name__ == '__main__':
    pytest.main(['-s','test_order.py'])