import requests
from day88.tools.log1 import Getlog,logger


class Base_Req1(object):

    def __init__(self):
        self.logger = logger
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}
        self.logger.info('实例化请求基础类')

    def post_template(self,data,url,session=requests.session()):
        url = self.ip + url
        print(f'url为{url}')
        resp = session.post(url=url, data=data, headers=self.headers)
        self.logger.info(f'请求成功：{resp.text}')
        return resp
if __name__ == '__main__':
    url = '/mtx/index.php?s=/index/user/login.html'
    data = {'accounts': 'bull', 'pwd': '123456'}
    req = Base_Req1()
    res = req.post_template(data)
    print(res.json())