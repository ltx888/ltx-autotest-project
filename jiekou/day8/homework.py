#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: homework.py
# @Author: Bull
# ---

# 问题：
# 1.括号内有时需要加self有时不需要加，为什么？
# 1.1这个知识点是"面向对象"里边描述的,所有类之中的方法需要加self函数.
# 1.2类之中的方法,仅只下辖的第一层.

# 2.yaml怎么使用
# 2.1yaml文件和@pytest.mark.parametrize是两种参数化方式
# yaml:把代码中的变量,储存到yaml文件.
# 目的:是把容易变化的变量,抽离出来.方便维护

# @pytest.mark.parametrize:向测试方法填充不同的入参\出参\检查点信息(变量).
# 目的:是复用一个检查方法(也就是pytest中的一个case)
# 他们的交集是可以使用yaml储存参数化的数据

# 使用yaml数据分离写用例的时候怎么使用pytest的ids

# 3.log是要在每个case里面都添加吗？
# 3.1写日志的目的是为了调错,所以需要调错就要加日志.
# 3.2可以考虑放到base(基类)中写日志.

# 4.为什么setup里调用基类就要先实例化，但是在测试方法里面调用基类可以直接self
# 这里,setup是一个特殊的方法.pytest会使用hook的方式处理它.不能按照普通类方法去使用它
#
# 5.基础类定义了__init__方法，但是测试类中调用基础类的时候报错（测试类里并没有定义过init）：
# 解决方案:不能在pytest测试类中写init方法
# 原因:会阻止pytest的init方法执行


