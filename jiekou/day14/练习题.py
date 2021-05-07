#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# @author: Bull
# @Time:   3月 13, 2021
# @Copyright：北京码同学网络科技有限公司

# 1.从首页使用左侧弹层进入手机商品页面-首页对象来实现

# 2.从手机商品页面,购买任意一件商品点击进入商品详情-商品页面来实现

# 3.购买商品-商品详情页面来实现

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:return 0
        # 双指针实现
        point_haystack = 0
        point_needls= 0

        N = len(haystack)
        n = len(needle)
        # N = N - n
        print(f'N:{N}')

        # 遍历范围是:haystack长度-needle长度+1
        range_v=N - n + 1
        while point_haystack < range_v:
            while point_haystack < range_v and haystack[point_haystack]!=needle[point_needls]:
                print(f'初级筛选:{point_haystack}')
                point_haystack+=1

            haystack_temp_point = point_haystack


            while haystack_temp_point < N and point_needls < n and haystack[haystack_temp_point]==needle[point_needls]:
                print(f'二级筛选{haystack_temp_point}')
                haystack_temp_point += 1
                point_needls += 1


            if point_needls == n:
                return point_haystack
            point_needls = 0
            point_haystack +=1

        return -1

obj = Solution()
a = 'bbaa'
b = 'aab'
print(obj.strStr(a, b))