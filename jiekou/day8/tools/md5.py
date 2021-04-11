#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: md5.py
# @Author: Bull
# ---
import hashlib,base64

class Encrypt():
    def __init__(self,string):
        self._string = string.encode('utf-8')

    def md5(self):
        # 封装md5加密
        # md5_string = hashlib.md5(self._string)
        # return md5_string.hexdigest()
        try:
            md5_string = hashlib.md5(self._string)
            return md5_string.hexdigest()
        except:

            return 'md5字串加密失败'

    def base64encode(self):
        try:
            return base64.b64encode(self._string).decode('utf-8')
        except:
            return 'base64加密失败'

    def base64decode(self):
        try:
            return base64.b64decode(self._string).decode('utf-8')
        except:
            return 'base64解密失败'


if __name__ == '__main__':
    string = '待加密的字符串'
    e = Encrypt(string)
    print(f'md5:{e.md5()}')
    print(f'base64encode:{e.base64encode()}')
    #假设需要加密一个token
    key = 'keyasd88332376'
    #用户唯一表示，一般是userid 或者 手机号这样的唯一
    userid = '6654'
    #加入一个时间戳，来和服务器时间做比较。如果他们的差大于“过期时间”，那么这条数据就会报错“超时”
    time = '202010251120'
    #拼接token字符串
    token = key + time + userid
    print(f'token:{token}')
    e = Encrypt(token)
    token_md5 = e.md5()
    print(f'token_md5:{token_md5}')