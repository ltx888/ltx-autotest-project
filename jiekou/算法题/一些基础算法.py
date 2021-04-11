# # 计算1-100 的累积和
# # 定义一个出始变量
# n = 1
# sum = 0
# # 条件
# while n <= 100
#     # 执行代码逻辑
#     sum += n
#     n += 1
# print(sum)
#
# # 计算1-100范围内的偶数和
# n = 1
# sum = 0
# while n <= 100:
#     if n % 2 == 0:
#         sum += n
#     n += 1
# print(sum)

# 输出一行5颗星
# i = 1
# while i <= 5:
#     i +=1
#     print('*******')

# 打印三角形
# i= 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         # print()里面加入 end='' 结束
#         print('*',end='')
#         j += 1
#     # print()默认操作等于换行
#     print()
#     i += 1

str ='hello haha\t world\t hi\tnihao beautiful\t haha\nok'
str2 = str.replace(' ','').replace('\t','').replace('\n','')

print(str2)