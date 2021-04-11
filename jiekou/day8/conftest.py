#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: conftest.py
# @Author: Bull
# ---
import sys,os
path = os.path.join(os.path.dirname(__file__),'../')#获取当前的绝对路径
sys.path.append(path)#把当前路径加入到python-path