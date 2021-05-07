import pytest
import html
import allure
from day88.api.login_api1 import login_api1

class Test_login1:

    def test_case1(self):
        # 实例化login api类
        obj = login_api1()
        # 接口返回数据转换程字典格式，进行断言
        resp = obj.login1()
        resp = resp.json()
        msg = resp['msg']
        assert msg =='登录成功'

if __name__ == '__main__':
    pytest.main(['-s','test_login1.py'])