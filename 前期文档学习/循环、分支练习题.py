#例1：100以内的素数，要求：素数指的是只能被 1 和自身整除的正整数（不包括 1）
# is_prime=True
# for x in range(1,101):
#     for i in range(2,101):
#         if x%i==0:
#             is_prime=False
#             break
#         if is_prime:
#             print(f'{x}')
#         else:
#             break
from scipy.ndimage import watershed_ift

# for x in range(2,100):
#     is_prime = True
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(x)

#例2：斐波那契数列，要求：输出斐波那契数列中的前 20 个数。
# 数列的前两个数都是 1，从第三个数开始，每个数都是它前面两个数的和。按照这个规律，斐波那契数列的前 10 个数是：`1, 1, 2, 3, 5, 8, 13, 21, 34, 55`。
# x,y=1,1
# count=0
# for i in range(1,x):
#     for j in range(1,y):
#         z=i+j
#         print(f'{z}')
#         x,y=j+z,i+z
#         count+=1
#     if count>=20:
#         break

# x,y=0,1
# for _ in range(20):
#     x,y=y,x+y
#     print(x)

#例3：寻找水仙花数，它是一个N位非负整数，其各位数字的N次方和刚好等于该数本身
#要求：找出 100 到 999 范围内的所有水仙花数。
#提示：//和%运算符
#x=634//100 可以得到百位
#x=634//10%10 可以得到十位
#x=152%10 可以得到个位
#print(x）
#测试:
# x=153//100
# y=153//10%10
# z=153%10
# w=x**3+y**3+z**3
# print(w)

#(i//100)**3 百位
#(i//10)%10**3 十位
#(i%10)**3 个位

# 自己写的
# for i in range(100,1000):
#     x=(i//100)**3
#     y=(i//10)%10**3
#     z=(i%10)**3
#     if x+y+z==i:
#         print(i)

# for i in range(100,1000):
#     x=i%10
#     y=i//10%10
#     z=i//100
#     if i==x**3+y**3+z**3:
#         print(i)

#例4：百钱百鸡问题：
#公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
# r,h,c=0,0,0 #表示数量
# num,money=0,0
# for r in range(0,100):
#     for h in range(0,100):
#         for c in range(0,100):
#             money=r*5+h*3+c*(1/3)
#             num=r+h+c
#             if money==num==100:
#                 print(f'公鸡有{r}只,母鸡有{h}只,小鸡有{c}只')

# for x in range(0, 21):
#     for y in range(0, 34):
#         for z in range(0, 100, 3):
#             if x + y + z == 100 and 5 * x + 3 * y + z // 3 == 100:
#                 print(f'公鸡: {x}只, 母鸡: {y}只, 小鸡: {z}只')

#例5 CRAPS赌博游戏
# 玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
# 玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
# 玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。
# 为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
# 每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
# 如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）。
#错误1 and和or用法
#原来写的：
#第一遍：
#num2==2 and 3 and 12:
#第二遍：
#num2==2 and num2==3 and num2==12:
# import random
# # num1=random.randint(2,12)
# # num2=random.randint(2,12)
# money=1000
# player=True
# while player:
#     bet = int(input('你下注的金额：'))
#     if bet<=0 or bet>money:
#         print('下注金额无效，请重新输入')
#         continue
#
#     num1 = random.randint(2, 12)
#     print(f'你第一次摇出的点数是:{num1}')
#     if num1==7 or num1==11:
#         money += bet
#         print(f'you win!你的资金有{money}')
#     elif num1==2 or num1==3 or num1==12:
#         money -= bet
#         print(f'you lose!,你的资金还剩{money}')
#     else:
#         num2 = random.randint(2, 12)
#         print(f'Game Again!你第二次摇出的点数是{num2}')
#         if num2==7:
#             money -= bet
#             print(f'you lose!你的资金还剩{money}')
#         elif num2==num1 :
#             money += bet
#             print(f'you win!你的资金有{money}')
#         else:
#             print(f'游戏继续!')
#     if money == 0:
#         print('你破产了!Game Over!')
#         player=False

# """
# Craps赌博游戏
#
# Version: 1.0
# Author: 骆昊
# """
# import random
#
# money = 1000
# while money > 0:
#     print(f'你的总资产为: {money}元')
#     # 下注金额必须大于0且小于等于玩家的总资产
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
#     first_point = random.randrange(1, 7) + random.randrange(1, 7)
#     print(f'\n玩家摇出了{first_point}点')
#     if first_point == 7 or first_point == 11:
#         print('玩家胜!\n')
#         money += debt
#     elif first_point == 2 or first_point == 3 or first_point == 12:
#         print('庄家胜!\n')
#         money -= debt
#     else:
#         # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
#         while True:
#             current_point = random.randrange(1, 7) + random.randrange(1, 7)
#             print(f'玩家摇出了{current_point}点')
#             if current_point == 7:
#                 print('庄家胜!\n')
#                 money -= debt
#                 break
#             elif current_point == first_point:
#                 print('玩家胜!\n')
#                 money += debt
#                 break
# print('你破产了, 游戏结束!')



























