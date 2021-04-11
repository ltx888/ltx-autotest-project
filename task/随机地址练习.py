import random

class address():

    v0 = ['北京市','河北省','河南省']
    v1 = {'北京市':['北京市'],'河南省':['郑州市','开封市','登封市','洛阳市'],'河北省':['石家庄市','邢台市']}
    v2 = ['龙门街道','户部巷','滨河大道','中心路','吉林大道']
    v3 = ['101号3门405','底商56']
    av0 = random.choice(v0)
    print(av0)
    av1 = random.choice(v1[av0])
    print(av1)
    av2 = random.choice(v2)
    av3 = random.choice(v3)
    add = av0 + av1 + av2 + av3
    print(add)