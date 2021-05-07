#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: flask_demo_tools.py
# @Author: Bull
# ---
# 处理读写数据
import csv

def reg_reight(name,password):
    path = 'reg_data.csv'
    with open(path,'a+',newline = '',encoding='utf-8')as file:
        reg_write_csv = csv.writer(file)
        data_row = [name,password]
        reg_write_csv.writerow(data_row)

#用来读取数据的函数,并且用"姓名"作为键储存
def read_all_data(path = 'reg_data.csv'):
    res_dict = {}
    with open(path,'r',encoding='utf-8')as file:
        data = csv.reader(file)
        for row in data:
            res_dict[row[0]]= row[1]
    return data#res_dict


if __name__ == '__main__':
    # reg_reight('张三','123456')
    print(read_all_data())