#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: 算法练习.py
# @Author: Bull
# ---
from typing import List

def majorityElement_V1( nums: List[int]) -> int:
    res = []           #定义一个变量,来存结果
    len_n = len(nums)#求出 数组 中的元素数量
    # print(f'n的长度是:{len_n}')
    # print(n.count(5))
    # 思考:
    # 我可以遍历这个 数组
    # 检查每一个数字出现的次数 是否大于 n/2
    # 出现的次数,list.count(i)
    for i in nums:
        if nums.count(i) > len_n / 2:
            res.append(i)
    res = set(res)
    return res

# n = [1,2,3,4,5,5,4,4,7]
n = [2,2,1,1,1,2,2,7,8]
# print(majorityElement_V1(n))


def majorityElement_V2(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


print(majorityElement_V2(n))