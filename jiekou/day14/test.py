import yaml
from day14.setting import DIR_NAME
def dushu():
    path = DIR_NAME + '/case/testdata/test_login.yaml'
    f = open(path, 'r', encoding='utf-8')
    data = yaml.safe_load(f)
    return data['data']

list = dushu()
for i in list:
    username = i[0]
    kw = i[1]
    print(name)

