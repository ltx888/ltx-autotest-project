
import requests
import yaml

from day88.api.Base_Req1 import Base_Req1
from day88.setting1 import HEADERS, DIR_NAME
from day88.tools.log1 import Getlog

class login_api1(Base_Req1):
    def __init__(self):
        path = DIR_NAME + '/api/login_api1.yaml'
        f = open(path, 'r' ,encoding='utf-8')
        self.data = yaml.safe_load(f)
        self.url = self.data['url']
        self.logger = Getlog().get_logger()

    def login1(self,session=requests.session()):
        resp_login = session.post(url=self.url, data=self.data['data'],headers= HEADERS)
        print(resp_login.text)
        return session, resp_login
if __name__ == '__main__':
    obj = login_api1()
    obj.login1()

