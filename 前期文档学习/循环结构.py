# import time
# for _ in range(5):
#     print('Hello,world')
#     time.sleep(1)

# 1-50 整数求和
# total=0
# for i in range(1,101):
#     total+=i
# print(total)

# #1-100 偶数求和
# total=0
# for i in range(1,101):
#     if i%2==0:
#         total+=i
# print(total)

# total=0
# for i in range(2,11,2):
#     total+=i
# print(total)


# total=0
# i=1
# while True:
#     total+=i #与total=total+i一样用法
#     i+=1
#     if i>100:
#         break
# print(total)

#1-100 偶数求和
# total=0
# i=0
# while i<=100:
#     i+=1
#     if i%2==0:
#         continue
#     total+=i
# print(total)

# total=0
# for i in range(1,101):
#     if i%2==0:
#         continue
#         total+=i#(记得缩进)
# print(total)

#九九乘法表 嵌套循环
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()

#要求输入一个大于1的数字，判断它是不是素数
# x=int(input('x='))
# is_prime=True
# for i in range(2,x+1):
#     if x%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print(f'{x}是一个素数')
# else:
#     print(f'{x}不是一个素数')

#最大公约数，要求：输入两个大于0的正整数，求两个数的最大公约数。
#(1) x=int(input('x='))
# y=int(input('y='))
# gcd=0
# for i in range(1,min(x,y)+1):
#     if x%i==0 and y%i==0:
#         gcd=i
# print(f'{x}和{y}的最大公约数是{gcd}')
#(2)
# x=int(input('x='))
# y=int(input('y='))
# for i in range(x,1,-1):
#     if x%i==0 and y%i==0:
#         break
# print(f'{i}是{x}和{y}的最大公约数')
#（3）
# x=int(input('x='))
# y=int(input('y='))
# while y%x!=0:
#     x,y=y%x,x
# print(f'{x}是最大公约数')
#4猜数字
# import random
# answer=random.randint(1,10)
# count=0
# while True:
#     count+=1
#     num=int(input('请输入你猜测的数字：'))
#     if num<answer:
#         print('猜小了')
#     elif num>answer:
#         print('猜大了')
#     else:
#         print('恭喜你猜对了！')
#         break
# print(f'一共用了{count}次')

import random

from fontTools.misc.plistlib import end_key

answer=random.randint(1,100)
x=1
y=100
count=0
while True:
    count+=1
    num=int(input(f'请输入一个数字,范围为（{x}，{y}）:'))
    if num<answer:
        x=num
        print(f'不好意思，猜小了！范围为({x},{y})')
    elif num>answer:
        y=num
        print(f'不好意思，猜大了！ 范围为（{x},{y}）')
    else:
        print(f'恭喜你，猜对了！一共用了{count}次')
        break

