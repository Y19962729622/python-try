# def fac(num):
#     result=1
#     for i in range(2,num+1):
#         result*=i
#     return result
# from math import factorial
# m=int(input('m='))
# n=int(input('n='))
# print(factorial(m)//factorial(n)//factorial(m-n))
from pandas.io.stata import StataValueLabel


# def make_judgement(*,a,b,c):
#     return a+b>c and a+c>b and b+c>a
# print(make_judgement(2,4,5))
# print(make_judgement(1,6,7))
# print(make_judgement(a=1,b=6,c=7)) #False
# print(make_judgement(a=2,b=4,c=5)) #True

# from random import randint
# #n为色子个数
# def roll_dice(n=2):
#     total=0
# #总数一开始为0，要算两个色子的总点数
#     for _ in range(n):
#         total+=randint(1,6)
#     return total
# print(roll_dice())
# print(roll_dice(3))

# def sum(a=0,b=0,c=0):
#     return a+b+c
# print(sum())  #0
# print(sum(1)) #1
# print(sum(2)) #2
# print(sum(3,4)) #7
# print(sum(3,4,5)) #12
# def add(*args):
#     print(args)
#     total=0
#     for i in args:
#         total+=i
#     return total
# print(add()) #() 0
# print(add(1,2,3,4,5)) #(1,2,3,4,5) 15
# def foo(*args,**kwargs):
#     print(args)   #(9.9, 10, 'name', False)
#     print(kwargs) #{'age': 18, 'height': 185}
# foo(9.9,10,'name',False,age=18,height=185)

# def f(x,y,*args,**kwargs):
#     # print(x,y,args) #1 2 (3, 4)
#     # print(kwargs)   #{'a': 20, 'b': 40}
#     print(x,y,*args,*kwargs.values()) #1 2 3 4 20 40
# f(1,2,3,4,a=20,b=40)

# import module1 as m1
# import module2 as m2
# module1.foo()#Nice to meet you!
# module2.foo()#I am glad to meet you!
# m1.foo() #Nice to meet you!
# m2.foo() #I am glad to meet you!

# from module1 import foo as f1
# from module2 import foo as f2
# f1() #Nice to meet you!
# f2() #I am glad to meet you!

# #例1：随机验证码
# #要求：设计一个生成随机验证码的函数，
# # 验证码由数字和英文大小写字母构成，长度可以通过参数设置。
# import random
# import string
# ALL_CHARS=string.digits+string.ascii_letters+string.punctuation
# def generate_code(*,code_len=6):
#     """
#     生成指定长度的验证码
#     :param code_len: 验证码的长度（默认4个字符）
#     :return: 由大小写英文字母和数字构成的随机验证码字符串
#     """
#     return ''.join(random.choices(ALL_CHARS,k=code_len))
# for _  in range(6):
#     print(generate_code())

#输入m和n，计算组合数C(m,n)的值
# def fac(num):
#     result = 1
#     for i in range(1,num+1):
#         result*=i
#     return result
# m=int(input('m='))
# n=int(input('n='))
# print(fac(m)//fac(n)//fac(m-n))

#练习题：封装通用日志打印函数
#定义参数，设置日志的默认值
# def log_print(msg,level='info'):
# #定义级别
#     valid_level=['debug','info','warning','error']
# #判断输入的值是否合法,不合法，按照info处理
#     if level not in valid_level:
#         level='info'
# #设置输出格式，级别名称自动大写
#     print(f'{[level.upper()]}{msg}')
# print('没有问题')
# log_print('测试失误',level='warning')
# log_print('出错啦',level='error')

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
# 你可以按任意顺序返回答案。
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         hash_map={}
#         for i in range(len(nums)):
#             need=target - nums[i]
#             if need in hash_map:
#                 return [hash_map[need],i]
#             else:
#                 hash_map[nums[i]]=i
# print(Solution().twoSum([2,7,11,15],9))






