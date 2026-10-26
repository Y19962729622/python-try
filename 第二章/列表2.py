# art= ['书法', '绘画', '雕塑', '音乐', '舞蹈','绘画','绘画']
# PE=['football','basketball','table tennis','Walking','running']
import random

# art.append('表演')
# print(art) #['书法', '绘画', '雕塑', '音乐', '舞蹈', '表演']
# art.insert(3,'钢琴')
# print(art) #['书法', '绘画', '雕塑', '钢琴', '音乐', '舞蹈', '表演']

# if '书法' in art:
#     art.remove('书法')
# if 'write' in art:
#     art.remove('write')
# print(art)
# art.pop()
# PE=art.pop(1)
# print(PE)
# art.append(PE)
# print(art)
# art.clear()
# print(art)

# del art[3]
# print(art)

# print(art.index('雕塑')) #2
# print(art.index('音乐',2)) #3
# print(art.index('绘画',4)) #5
# print(art.index('书法',5)) #ValueError: '书法' is not in list
# print(art.count('绘画')) #3

# art.sort()
# print(art) #['书法', '绘画', '绘画', '绘画', '舞蹈', '雕塑', '音乐']
# PE.sort()
# print(PE) #['Walking', 'basketball', 'football', 'running', 'table tennis']
# PE.reverse()
# print(PE) #['table tennis', 'running', 'football', 'basketball', 'Walking']
# 创建一个取值范围在`1`到`99`且能被`3`或者`5`整除的数字构成的列表。
# num=[ i for i in range(1,100) if i%3==0 and i%5==0 ]
# print(num)

#有一个整数列表`nums1`，创建一个新的列表`nums2`，`nums2`中的元素是`nums1`中对应元素的平方。
# nums1=[2,4,6,8,10,12]
# nums2=[num**2 for num in nums1]
# print(nums2) #[4, 16, 36, 64, 100, 144]

# 有一个整数列表`nums1`，创建一个新的列表`nums2`，将`nums1`中大于`50`的元素放到`nums2`中。
# nums1=[29,47,45,76,38,99,87,105]
# nums2=[num for num in nums1  if num>50] #[76, 99, 87, 105]
# print(nums2)
# 我们想保存5个学生3门课程的成绩，可以用如下所示的列表。
# score=[[100,95,100],[97,98,90],[90.5,100,97],[90,98,95],[93,97,96]]
# print(score[2]) #[90.5, 100, 97]
# print(score[0][1]) #95
# 通过键盘输入的方式来录入3个学生2门课程的成绩并保存在列表中
# student=[]
# for _ in range(3):
#     temp=[]
#     for _ in range(2):
#         score=int(input('请输入学生成绩：'))
#         temp.append(score)
#     student.append(temp)
# print(student)
# 如果想通过产生随机数的方式来生成3个学生2门课程的成绩并保存在列表中，我们可以使用列表生成式，代码如下所示。
# student=[[random.randint(60,100) for _ in range (2)] for _ in range(3)]
# print(student)

# 每注投注号码由`6`个红色球和`1`个蓝色球组成。
# 红色球号码从`1`到`33`中选择，蓝色球号码从`1`到`16`中选择。
# 每注需要选择`6`个红色球号码和`1`个蓝色球号码。
# import random
# ball=[7]*6
# for _ in range(6):
#     red=random.randint(1,33)
#     ball.append(red)
#     for _ in range(1):
#         blue=random.randint(1,16)
#         ball.append(blue)

# import random
# red_ball=list(range(1,34))
# selected_balls=[]
# for _ in range(6):
# #用索引表示被选中球的位置
#     index=random.randint(0,len(red_ball))
# #把选中的球在原列表中删除并添加在新的列表中
#     selected_balls.append(red_ball.pop(index))
# #再对其进行排序，输出结果
# selected_balls.sort()
# #将选中的红色球输出
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[m',end=' ')
# blue_ball=random.randint(1,16)
# print(f'\033[34m{blue_ball:0>2d}\033[m',end=' ')

import random
# red_balls=list(range(1,34))
# selected_balls=[]
# for _ in range(6):
#     index=random.randint(0,len(red_balls)-1)
#     selected_balls.append(red_balls.pop(index))
# selected_balls.sort()
# for balls in selected_balls:
#     print(f'\033[31m{balls:0>2d}\033[0m',end=' ')
# blue_balls=random.randint(1,16)
# print(f'\033[34m{blue_balls:02d}\033[0m')

# red_balls=[i for i in range(1,34)]
# blue_balls=[i for i in range(1,17)]
# n=int(input('生成几注号码：'))
# for _ in range(n):
#     selected_ball=random.sample(red_balls,6)
#     selected_ball.sort()
#     for ball in selected_ball:
#         print(f'\033[31m{ball:0>2d}\033[0m',end=' ')
#     blue_ball=random.choice(blue_balls)
#     print(f'\033[34m{blue_ball:0>2d}\033[0m')

