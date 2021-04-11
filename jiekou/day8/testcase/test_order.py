#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: test_order.py
# @Author: Bull
# ---
import pytest

from day8.api.order_api import order_api


class Test_login:

    def test_case1(self):#登录成功
        obj = order_api()
        session,resp = obj.login_and_order()
        resp = resp.json()


if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])