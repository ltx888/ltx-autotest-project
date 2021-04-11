#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: test_login.py
# @Author: Bull
# ---
import pytest

from day8.api.login_api import login_api


class Test_login:

    def test_case1(self):#登录成功
        obj = login_api()
        session,resp = obj.login()
        resp = resp.json()
        msg = resp['msg']
        assert msg =='登录成功'

if __name__ == '__main__':
    pytest.main(['-s','test_login.py'])