# # 将一颗色子掷 6000 次，统计每种点数出现的次数。
# import random
# f1=0
# f2=0
# f3=0
# f4=0
# f5=0
# f6=0
# for i in range(6000):
#     i=random.randint(1,6)
#     if i==1:
#         f1+=1
#     elif i==2:
#         f2+=1
#     elif i==3:
#         f3+=1
#     elif i==4:
#         f4+=1
#     elif i==5:
#         f5+=1
#     elif i==6:
#         f6+=1
# print(f'抛出了{f1}次的1点')
# print(f'抛出了{f2}次的2点')
# print(f'抛出了{f3}次的3点')
# print(f'抛出了{f4}次的4点')
# print(f'抛出了{f5}次的5点')
# print(f'抛出了{f6}次的6点')


# item=[10,20,30,40,50]
# # item1=['看书','听音乐','看电影']
# item2=['100','99.9','加油','True','Chinese']
# print(30 in item)
# # print(item1)
# print('加油'not in item2)

# item=list(range(1,11))
# item1=list('love')
# item2=list(('sad and happy','I like you!','tomorrow'))
# print(item)
# print(item1)
# print(item2)

# item=[1,2,3,4,5]
# item1=[6,7,8,9,10]
# item2=['I','YOU','He','She']
# print(item+item1)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(item1+item2)#[6, 7, 8, 9, 10, 'I', 'YOU', 'He', 'She']
# item+=item2
# print(item)#[1, 2, 3, 4, 5, 'I', 'YOU', 'He', 'She']

# item=['I love you']#['I love you', 'I love you', 'I love you']
# print(item*3)

# item4=['dog','cat','pig','duck','bird']
# print(item4[2]) #pig
# item4[1]='cow'
# print(item4) #['dog', 'cow', 'pig', 'duck', 'bird']
# print(item4[-2])
# item4[-1]='sheep' #duck
# print(item4) #['dog', 'cow', 'pig', 'duck', 'sheep']
# item4=['dog','cat','pig','duck','bird']
# print(item4[1:3:1])#['cat', 'pig']
# print(item4[::1])#['dog', 'cat', 'pig', 'duck', 'bird']
# print(item4[1::2])#['cat', 'duck']
# print(item4[2:4])#['pig', 'duck']
# #print(item4[-3:-5]) 步长可以省略，但是记得是已经默认步长为1（从左往右读）
# print(item4[-5:-3])#['dog', 'cat']
# item4[2:5]=['apple','orange','banana']
# print(item4)#['dog', 'cat', 'apple', 'orange', 'banana']

# PE=['台球','足球','篮球','排球','羽毛球']
# for PE in PE:
#     print(PE)

import random
# face=list(range(1,7))
# f1,f2,f3,f4,f5,f6=0,0,0,0,0,0
# for i in range(6000):
#     if i==face[0]:
#         f1+=1
#     elif i==face[1]:
#         f2+=1
#     elif i==face[2]:
#         f3+=1
#     elif i==face[3]:
#         f4+=1
#     elif i==face[4]:
#         f5+=1
#     elif i==face[5]:
#         f6+=1
# print(f'{f1}=,{f2}=,{f3}=,{f4}=,{f5}=,{f6}=')

# import random
# times=[0]*6
# for _ in range(6000):
#     face=random.randint(1,6)
#     times[face-1]+=1
# for face in range(1,7):
#     print(f'色子{face}点，出现了{times[face-1]}次')

import random
#一个6个面的色子连续抛6000次
face=[random.randint(1,6) for _ in range(6000)]#如果只是这句，会出现6000个1~6
times=[face.count(i) for i in range(1,7)]
for face in range(1,7):
    print(f'色子{face}面出现了{times[face-1]}次')






