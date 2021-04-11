#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 知识点总结.py
# @Author: Bull
# ---

# 1.框架分层
# api\case\tools\log\report
# api层负责requests调用
# case层只负责组装业务,和写检查点
#
# 2.使用setting.py文件来储存公共变量

# 3.yaml文件读取的路径建议统一管理.例如放到setting.py中

# 4.关于日志多次打印
# 对于日志这个业务而言.我们只希望输出一个数据就足够了 → 单例模式:无论被实例化多少次,也只新建唯一的一个实例

# 5.pytest-allure装饰器
# 可以用来在测试报告中增加信息

# 6.有时运行case的时候,会报错"找不到模块"
# 6.1在框架根目录创建conftest.py 和 __init__.py
# 6.2在conftest.py加入:
# import sys,os
# path = os.path.join(os.path.dirname(__file__),'../')#获取当前的绝对路径
# sys.path.append(path)#把当前路径加入到python-path

# *7.pytest.ini的配置
# 可以对pytest的默认值进行设置.例如:
# [pytest]
# addopts = -s
# testpaths = ./scripts
# python_files = test_*.py
# python_classes = Test*
# python_functions = test_*