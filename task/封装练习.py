#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 封装练习.py
# @Author: Bull
# ---
# 目的:了解封装的语法 和 设计思路

import random
class random_data():#声明一个 类
    # 将原有的函数统一缩进,归属给"类"
    # f_name = ['张', '王', '李', '赵']
    # l_name = ['爱梅', '志芳', '光', '隽仙', '燕青', '振杰', '卫东']
    # path = 'random_name.txt'

    def __init__(self):
        self.f_name = ['张', '王', '李', '赵']
        self.l_name = ['爱梅', '志芳', '光', '隽仙', '燕青', '振杰', '卫东']

    def get_random_name(self):#改造原有函数,增加self入参
        # 根据中文名称的组成,先定义下姓氏 和 名
        res_name = ''
        #名称=随机姓氏+随机名称
        f = random.choice(self.f_name)
        l = random.choice(self.l_name)
        res_name = f + l
        return res_name

    def get_random_names(self,num=10):

        name_list = []
        for i in range(num):
            # print(i)
            t = self.get_random_name()
            name_list.append(t)

        return name_list

    def write_random_names(self,num=10):
        t_list = self.get_random_names(num)
        for i in t_list:
            with open(self.path,'a') as f:
                f.write(i)
                f.write('\n')

    def unique_names(self,num=10):#前置去重

        name_list = []#用来储存结果的列表
        i = 0   #循环表示
        while i < num:#循环的条件是 i 表示<10,并且这个 i 标识我们是可以控制(增减)的
            t = self.get_random_name()   #每一个循环获取1个随机的姓名
            if t not in name_list:  #如果当前随机的姓名变量-t,不在结果列表(也就是"唯一")
                name_list.append(t) #把它加到结果列表里
                i = i + 1           #手动增加一个 i 标识
            #如果不满足上边的 if 呢
    #怎么设计,让这个方法不会进入死循环

        return name_list

object = random_data() #进行实例化
# var = object.get_random_name()
# print(var)

# 封装有什么特别的好处?
# 封装可以包装更多逻辑

# 面向对象还有什么特别的好处?
# 继承 和 多态


var = object.unique_names()
print(var)