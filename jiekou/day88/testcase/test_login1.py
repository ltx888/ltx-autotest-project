import pytest
import html
from day88.api.login_api1 import login_api1
import allure



class Test_login1:

    @allure.story('测试allure')
    def test_case1(self):
        obj = login_api1()
        session,resp = obj.login1()
        resp = resp.json()
        msg = resp['msg']
        assert msg =='登录成功'

if __name__ == '__main__':
    pytest.main(['-s','test_login1.py'])