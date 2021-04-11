#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: admin_api.py
# @Author: Bull
# ---
from day8.api.Base_Req import Base_Req
from day8.setting import HEADERS

#利用基础类进一步简化
class admin_login_api(Base_Req):

    def admin_login(self):
        url = '/mtx/admin.php?s=/admin/login.html'
        data = {
            'username': 'shamo',
            'login_pwd': 123456,
        }
        resp = self.post_template(url=url,data = data)

        return resp

if __name__ == '__main__':
    obj = admin_login_api()
    resp = obj.admin_login()
    print(resp)