import requests
from day88.tools.log1 import Getlog,logger
from day88.setting1 import IP,HEADERS

class Base_Req1(object):

    def __init__(self):
        self.logger = logger
        self.logger.info('实例化请求基础类')
        self.ip = 'http://121.42.15.146:9090'
        self.headers = HEADERS


    # post 请求类
    def post_template(self,url,data,session=requests.session()):
        url = self.ip + url
        print(url)
        resp = session.post(url=url,data=data,headers=self.headers)
        self.logger.info(f'请求成功：{resp.text}')
        return resp


if __name__ == '__main__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = {'accounts': 'bull', 'pwd': '123456'}
    req = Base_Req1()
    res = req.post_template(url,data)
    print(res.json())