#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: flask_demo.py
# @Author: Bull
# ---
from flask import Flask,json,request,jsonify
#可以理解Flask是一个网站类
from day11.flask_demo.flask_demo_tools import read_all_data,reg_reight

app = Flask(__name__)
#app是一个网站实例

# 使用flask首先编写"路由"
# 路由:是一个web app的接口清单
# 使用@app.route('路由地址',method=['GET'])装饰器来编写路由
# @app.route('/',methods=['GET'])
# def api_test():#在路由装饰器下方,编写一个用来处理业务功能的方法
#
#     return '一个练习用的接口'

@app.route('/register',methods=['POST']) #路由
def register():#注册逻辑
    # 1.接收入参
    data = json.loads(request.get_data(as_text=True)) #把入参都储存到data变量中
    # 2.解析入参
    # 这个接口计划有name 和 pwd两个入参
    try:
        name = data['name']
        pwd = data['pwd']
        if len(name) == 0 or len(pwd)<6:
            dict = {'message': '入参长度异常', 'code': -4}
            return jsonify(dict)
    except Exception as e:
        print('入参异常,可能缺少参数')
        dict = {'message': '可能缺少参数导致解析失败', 'code': -3}
        return jsonify(dict)


    # 3.处理业务逻辑:存数据
    # 思路:
    #     1.注册的数据可以存到csv文件
    #     2.重复的数据需要返回错误信息
    #     3.异常情况的处理

    # 发现问题:
    # 1.重复数据怎么处理
    #     需判断数据重复,需要预读一下数据
    # 2.其他异常
    # 需要实现读取数据的逻辑
    try:    #它可以捕获"读取数据"中可能异常
        user_data = read_all_data()
        if name in user_data:#如果尝试注册的"姓名"已经存在.就提示"用户已注册"
            # 组装这种异常情况的返回值
            dict = {'name': name, 'message': '用户已注册,请尝试登录', 'code': -1}
            return jsonify(dict)
    except Exception as e:
        print(f'发生异常,原因是{e}')
        dict = {'message': f'服务器处理异常,信息{e}', 'code': -2}
        return jsonify(dict)

    try:
        reg_reight(name, pwd)
        # 4.组装返回值
        dict = {'name': name, 'message': '注册成功', 'code': 200}
        return jsonify(dict)  # 使用jsonify返回json格式的数据
    except Exception as e:
        print(f'发生异常,原因是{e}')
        dict = {'message': f'写入数据时发生了异常,信息{e}', 'code': -4}
        return jsonify(dict)

@app.route('/login',methods=['POST']) #路由
def login():
    # 1.接收参数
    # 2.解析参数
    # 3.判断用户名密码是否一致
    #     1.一致-登录成功
    #     2.密码错误
    #     3.用户名错误
    #     4.未知异常

    # 1.接收参数
    data = json.loads(request.get_data(as_text=True))  # 把入参都储存到data变量中
    # 2.解析参数
    try:
        name = data['name']
        pwd = data['pwd']
        if len(name) == 0 or len(pwd)<6:
            dict = {'message': '入参长度异常', 'code': -4}
            return jsonify(dict)
    except Exception as e:
        print('入参异常,可能缺少参数')
        dict = {'message': '可能缺少参数导致解析失败', 'code': -3}
        return jsonify(dict)

    # 3.判断用户名密码是否一致
    try:
        user_data = read_all_data()
        #     1.一致-登录成功
        if name in user_data and pwd == user_data[name]:
            dict = {'name':name,'message': '登录成功', 'code': 200}
            return jsonify(dict)
        #     2.密码错误
        elif name in user_data and pwd != user_data[name]:
            dict = {'name':name,'message': '密码错误', 'code': 201}
            return jsonify(dict)
        #     3.用户名错误
        elif name not in user_data:
            dict = {'name':name,'message': '用户名错误', 'code': 202}
            return jsonify(dict)
        #     4.未知异常
    except Exception as e:
        dict = {'message': '发生未知异常', 'code': -10}
        return jsonify(dict)

#启动flask服务的一种方式
if __name__ == '__main__':
    app.run(port=5000,debug=True)