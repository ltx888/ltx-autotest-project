# # import random
# #
# # x = random.randint(1,5)
# # y = 0
# # while x < 100:
# #     y = input('请输入数字：')
# #     y = int(y)
# #     print(x)
# #     if y == x:
# #         print('恭喜你，猜中啦！！！！是！')
# #         break
# #
# age = 3
# name = '张三'
# # print('我的名字叫%s' % name)
# # print('我的年龄是%d' % age)
# # print(f'我的名字{name}风')
# # print(f'我的年龄是{age+1}')
# print('我的姓名是{},我的年龄是{}'.format(name,(age+3)))
# print('输出内容')
#
# str = 'Runoob'
# print(str)
# print(str[0:-1])
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str[1:5:2])
# print(str *  2)
# print(str + '你好')
# print('------------------------------')
# print('hello\nrunoob')
# print(r'hello\nrunoob')
# input('\n\n按退出')

# import  sys
# x = 'runoob'
# sys.stdout.write(x + '\n')
# import  sys
# print('===================python import moudle')
# print('命令行参数为：')
# for i in sys.argv:
#     print(sys.argv)
#     print(i)
# print('\n python 路径为',sys.path)
# from sys import argv,path
# print('==========python from import===============')
# print('path:',path)

# class A:
#     pass
# class B(A):
#     pass
# del A()
# print(isinstance(B(),A))
# list = [ 'abcd' , 784 , 2.23, 'runoob' , 70.2]
# tinylist = [123, 'runoob']
# print(list)
# print(list[1])
# print(list[1:3])
# print(list[2:])
# print(tinylist * 2)
# print(list + tinylist)
# print(list[0:-2:2])
# print(list[0:-2])
# a = [1 ,2 ,3, 4, 5, 6]
# dfdfd
#  [[[[]]]]
# a = 1
# while a < 7:
#     if a % 2 == 0:
#         print(a, "is even")
#     else:
#         print(a, "is odd")
#     a += 1
# flag = False
# name = 'luren'
# if name == 'python':
#     print ('welcome boss')
# else:
#     print (f'名字是{name}')
#     print('名字是%s' % name)

# a = 'hello'
# b = 'python'
#
# print("a + b")
# print("a * 2 输出结果为：", a * 2)
# print("a[1] 输出结果为：", a[1])


# c = a+b
# print("1 - c 的值为：",c)
#
# c = a - b
# print("2 - c 的值为：", c)
# if(a == b):
#     print("1 - a 等于 b")
# else:
#     print("1 - a 不等于 b")


# a = 60
# b = 13
# c = 0
#
# c = a & b
# print("1 - c 的值为：", c)

# a = 10
# b = 10

# if(a and b):
#     print("1- 变量a 和 变量b 都为 true")
# else:
#     print("1- 变量a 和 变量b 都为true， 或者其中一个额变量为true")
#

# if(a is b):
#     print("a 与 b 有相同的变量表识")
# else:
#     print("a 与 b 没有相同的变量表识")
#
# print(id(a))
# print(id(b))

# print(round(9.5))
# a = ']]dfdf[[['
# print(a.center(40,'*'))
# print(a.count('d'))
# print(a.encode('utf-8','strict'))
#
# str = 'Runoob example...wow!!!'
# suffix = '!!!'
# print(str.endswith('!!!',1,10))
# str = "runoob\t12345\tabc"
# print("原始字符：", str)
# print('替换\\t 符号：', str.expandtabs(2))