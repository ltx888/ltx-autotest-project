#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: allure报告相关的装饰器.py
# @Author: Bull
# ---
import requests
import allure
import pytest



class Test_login:
    ip = 'http://121.42.15.146:9090/mtx/'

    @allure.title('自定义的测试标题')
    @allure.story('登录功能点')
    @allure.severity('阻塞级别')
    @pytest.mark.parametrize('accounts,pwd,exp', [('bull', '123456', '登录成功')])
    def test_Decorator (self, accounts, pwd, exp):
        # 登录接口的url
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'accounts': accounts, 'pwd': pwd}
        r = requests.post(url=url, data=data, headers=headers)
        # print(r.text)
        res = r.json()
        print('头信息')
        print('*'*40)
        print(r.cookies.items())
        assert exp == res['msg']

    @pytest.mark.parametrize('accounts,pwd,exp', [('bull', '123456', '登录成功')])
    def test_No_Decorator(self,accounts, pwd, exp):
        # 登录接口的url
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {'X-Requested-With': 'XMLHttpRequest'}
        data = {'accounts': accounts, 'pwd': pwd}
        r = requests.post(url=url, data=data, headers=headers)
        # print(r.text)
        res = r.json()
        print('头信息')
        print('*'*40)
        print(r.cookies.items())
        assert exp == res['msg']

