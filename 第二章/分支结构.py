# #计算BMI，公式体重/身高的平方
# weight=float(input("请输入你的体重（kg）："))
# height=float(input("请输入你的身高(cm)："))
# bmi=weight/(height/100)**2
# print(f'{bmi=:.1f}')
# if 18.5<=bmi<24:
#     print('你的身材很棒') 24,27,30,35

# weight=float(input('请输入你的体重（kg）:'))
# height=float(input('请输入你的身高（cm）:'))
# bmi=weight/(height/100)**2
# print(f"{bmi=:.1f}")
# if bmi<18.5:
#     print("宝贝，你有点过轻喽")
# elif bmi<24:
#     print("同学，你的身材很棒哦~")
# elif bmi<27:
#     print("亲爱的，有点小胖，不过我喜欢哦~")
# elif bmi<30:
#     print("您好，正式通知您，你已经到中度肥胖的程度，建议减肥")
# elif bmi<35:
#     print("这位同志，饭菜虽好吃，但吃多了是身体的负担，您已经到重度肥胖的程度了，建议立刻减肥，再通知一遍，立刻减肥，这不是儿戏")
# else:
#     print("严重肥胖，立刻逮捕！！！")

# weight=float(input('请输入你的体重（kg）:'))
# height=float(input('请输入你的身高（cm）:'))
# bmi=weight/(height/100)**2
# print(f"{bmi=:.1f}")
# match bmi:
#     case x if 18.5<=x<24:
#         print("宝贝，你有点轻喽")
# date=int(input('请输入今天周几：'))
# match date:
#     case 1:
#         print('有早八')
#     case 2:
#         print('9点上课')
#     case 3:
#         print('今天只有一节课')

# num=int(input('请输入一个数字：'))
# match num:
#     case 1|3|5|7|9:
#         print('该数字是个奇数')
#     case 2|4|6|8|10:
#         print('该数字是个偶数')
#     case _:
#         print('其他')

#关于if和match分支语句的练习
# x=float(input('x='))
# if x>1:
#     y=3*x-5
# elif -1<=x<=1:
#     y=x+2
# else :
#     y=5*x+3
# print(f"{y=}")

# x=float(input("x="))
# match x:
#     case a if a>1:
#         y=3*a-5
#     case a if -1<=a<=1:
#         y=a+2
#     case a if x<-1:
#         y=5*a+3
# print(f'{y=}')

#百分制成绩转换成等级if分支语句
# x=float(input('请输入你的成绩：'))
# if x>=90:
#     grade='A'
# elif 80<=x<90:
#     grade='B'
# elif 70<=x<80:
#     grade='C'
# elif 60<=x<70:
#     grade='D'
# else:
#     grade='E'
# print(grade)
#match分支语句
# x=float(input('请输入你的成绩：'))
# match x:
#     case a if x>=90:
#         grade="A"
#     case a if 80<=x<90:
#         grade="B"
# print(grade)

# #三角形
# a=float(input('a='))
# b=float(input('b='))
# c=float(input('c='))
# if a+c>b and a+b>c and b+c>a:
#     perimeter=a+b+c
#     print(f'三角形的周长:{perimeter}')
#     s=(a+b+c)/2
#     area=(s*(s-a)*(s-b)*(s-c))**0.5
#     print(f'三角形的面积:{area}')
# else:
#     print('这三条边不能构成三角形')