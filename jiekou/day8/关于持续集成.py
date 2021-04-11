#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 关于持续集成.py
# @Author: Bull
# ---
# 对测试来说:
# 把执行自动化测试的步骤,交给计算机

# 对项目来说:
# 我们需要一个手段,来支持大规模的合作
# 持续集成就是说:强制要求开发人员,每天至少合并一次代码
# 每次集成,要求必须有测试手段(就是自动化测试)

# 实践:
# 1.需要使用git来实现自动获取最新测试脚本
# 1.1把本地的代码用git进行管理
#     git init
#     git add .
#     git commit -m 初始化

# 1.2把本地代码推送到远程仓库
# 免费开源的远程仓库服务:github\gitlab\gitee
#     注册一个git托管平台
#     在页面上新建一个仓库
#     按照提示中的"已有仓库"执行命令
# 1.3让jenkins从远程仓库获取代码
# 第一步:让linux拉取代码
# 安装git
# 使用克隆命令拉取代码
# git clone https://gitee.com/cowboy231/pytest_stu.git

# 第二步:让jenkins执行获取代码的linux命令

# jenkins机器,实际上是负责调度任务的.所以干活的应该是"节点"


