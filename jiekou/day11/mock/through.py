#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: through.py
# @Author: Bull
# ---
# 实现各种透传方法
import requests
from flask import json,make_response
url_true = 'http://127.0.0.1:5000/' #把真实服务的地址维护在这

# 参数透传
def pass_through(url,data):
    url = url_true + url            #拼接要透传的url
    print(f'透传的url是:{url}')

    res = requests.post(url,json=data)   #使用requests库去请求"真实"接口

    resp = make_response(res.json())    #对requests响应结果进行格式处理,使他满足flask响应数据的格式要求

    return resp             #返回响应

#接口级别的透传:没有实现mock的接口,就去调用真实接口
def passThroughRe(url,data):
    url = url_true + url            #拼接要透传的url
    print(f'透传的url是:{url}')

    res = requests.post(url,json=data)   #使用requests库去请求"真实"接口

    resp = make_response(res.json())    #对requests响应结果进行格式处理,使他满足flask响应数据的格式要求

    return resp             #返回响应