#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: mock_server.py
# @Author: Bull
# ---
#这个mock的业务背景:
# "注册于登录"接口服务要增加一些场景.例如'被锁定','黑名单','密码错误次数超限'


from flask import Flask,json,request,jsonify

from day11.mock.through import pass_through, passThroughRe

app = Flask(__name__)

@app.route('/login',methods=['POST']) #路由
def login():
    # 1.接收入参
    data = json.loads(request.get_data(as_text=True))  # 把入参都储存到data变量中
    # 2.解析入参
    name = data['name']
    pwd = data['pwd']
    # 3.实现预期的场景
    # 被锁定:这里我读取 data['name'],如果它是"被锁定",那就触发我的mock数据
    if name == '被锁定':
        return jsonify({'code':402,'name':name,'message':'用户已被锁定'})
    # 黑名单
    elif name == '黑名单':
        return jsonify({'code':403,'name':name,'message':'用户在黑名单中'})
    # 密码错误次数超限
    elif name == '错误次数超限':
        return jsonify({'code':405,'name':name,'message':'密码错误次数超限'})
    else:#去调用真实服务,并且把真实服务的响应返回出去
        url = 'login'
        res = pass_through(url=url,data=data )
        return res
    # 这里遇到一个问题,我们希望这个mock.既能返回"假数据"也能进行正常的逻辑调用.
    # 这里我的解决办法是使用"透传"

# 如果我们写mock服务,一般只mock一部分接口.那么没有进行mock的接口怎么办?
# 如果不在我们mock服务的路由中,那么也去'透传'给真实服务
@app.route('/<url_path>',methods=['POST'])  #这里我使用了flask的"动态路由"
def through(url_path):
    print(f'当前的{url_path}接口,没有在mock路由列表中.所以触发透传逻辑')
    # 获取入参
    data = request.get_json()
    #进行透传,获取响应
    resp = passThroughRe(url=url_path,data=data)
    return resp

if __name__ == '__main__':
    app.run(port=5001,debug=True)