# t1=(113,1113,360,700)
# t2=('Day and night','爱情树下',False,10,'sweet')
# #查看类型
# print(type(t1))#<class 'tuple'>
# print(type(t2))#<class 'tuple'>
# #查看元组中元素数量
# print(len(t1))#4
# print(len(t2))#5
# #索引运算
# print(t1[1])#1113
# print(t2[4])#sweet
# #切片运算
# print(t1[1:3:1])#(1113,360)
# print(t2[-1:-3:-1])#('sweet',10)
# #遍历运算
# for i in t2:
#     print(i)
# #成员运算
# print(25 in t1)#False
# print('money' not in t2 )#True
# #拼接运算
# print(t1+t2)#(113, 1113, 360, 700, 'Day and night', '爱情树下', False, 10, 'sweet')

#打包操作
# num=34,45,79,99,108,396
# # print(num)#(34, 45, 79)
# #解包操作
# h,i,j,*k=num
# print(h,i,j,k)#34 45 79 [99, 108, 396]

# a,*b,c=range(1,7)
# print(a,b,c)#1 [2, 3, 4, 5] 6
# a,b,c=[9,99,999]
# print(a,b,c)#9 99 999
# *a,b,c='tomorrow'
# print(a,b,c)#['t', 'o', 'm', 'o', 'r', 'r'] o w

# a=[12,23,34,45]
# print(tuple(a))#(12, 23, 34, 45)
# b=(98,87,76,65,54)
# print(list(b))#[98, 87, 76, 65, 54]

#字符串
# w1='早上好呀,'
# w2='一早起来肚子就不舒服。'
# w3='''
# 今天天气：
# 阴转小雨'''
# print(w1+w2+w3)

# s1='\'today is rainy day\''
# s2='\\今天是2026年10月18日\\'
# print(s1+s2) #'today is rainy day'\今天是2026年10月18日\

# s1='\it \is \time\to \read \now'
# s2=r'today \tomorrow \the day after tomorrow \the future'#today\tomorrow\the day after tomorrow\the future
# print(s1)
# print(s2)
# s1 = '\141\142\143\x61\x62\x63'
# print(s1) #abcabc

# s1='want'+' 👇 '+'get'+' have'+' a'+' do it '
# print(s1) #want 👇 get have a do it
# s2='if'+' you'+' really'*3+' want it'
# print(s2) #if you really really really want it
# s3=r"let 's do it"+'!'*3
# s1+=s3*3
# print(s1) #let 's do it!!!

# s1='于'
# s2='佳'
# s3='琪'
# print(ord(s1))#20110
# print(ord(s2))#20339
# print(ord(s3))#29738

# a1='see you later!'
# b1='looking forward to see you later!'
# print('at'in a1) #True
# print('oo'not in b1) #False
# print(a1 in b1) #True

# print(len(b1)) #33
# print(len('锲而不舍，滴水穿石')) #9

# y='3.1416926ABCDEFG'
# x=len(y)
# print(y[0],y[-x])  #3 3
# print(y[1],y[-x+1])#. .
# print(y[1:6:2])#.46
# print(y[:6:1]) #3.1416
# print(y[::-1]) #GFEDCBA6296141.3

# s1='never give up'
# s2='just do it'
# print(s1.capitalize())#第一个单词首字母大写，Never give up
# print(s2.title()) #每个单词的首字母都大写，Just Do It
# print(s2.upper()) #每个单词的每个字母都大写，JUST DO IT
# s3='OKAY'
# print(s3.lower()) #每个单词的每个字母都小写，okay
# print(s1)#never give up
# print(s2)#just do it

# w='Happy Birthday! Happy New Year!'
# print(w.find('py'))#3
# print(w.find('see'))#-1
# print(w.find('y',5))#13
# print(w.index('py'))#3
# print(w.count('py'))#2

# print(w.rfind('a'))  #28
# print(w.rindex('H')) #16

# r1='super38356'
# print(r1.startswith('98')) #False
# print(r1.endswith('38356'))#True
# r2='10JQK12'
# print(r2.isdigit())#False
# print(r2.isalpha())#False
# print(r2.isalnum())#True

# h='明天放假'
# print(h.center(10,'*'))#***明天放假***
# print(h.rjust(12,'!'))#!!!!!!!!明天放假
# print(h.ljust(8,'^'))#明天放假^^^^
# print('666'.center(9,'!'))#!!!666!!!
# print('88888'.zfill(13))#0000000088888

# a=321
# b=123
# print('%d*%d = %d'%(a,b,a*b))#321*123 = 39483
# print('{}*{}={}'.format(a,b,a*b))#321*123=39483
# s1=' yu  jia  qi '#yu  jia  qi
# print(s1.strip())
# s2='#TOT#'
# print(s2.lstrip('#'))#TOT#
# print(s2.rstrip('T'))#TTo#TOT#o

# s='very good'
# print(s.replace('o','@'))#very g@@d
# print(s.replace('o','@',1))#very g@od

# q='see!you!tomorrow'
# p=q.split('!')
# print(p) #['see', 'you', 'tomorrow']
# s=q.split('!',1)
# print(s) #['see', 'you!tomorrow']
# print(p) #['see', 'you', 'tomorrow']
# print('~'.join(p)) #see~you~tomorrow
a='于佳琪'
b=a.encode('utf-8')#b'\xe4\xba\x8e\xe4\xbd\xb3\xe7\x90\xaa'
print(b)
print(b.decode('utf-8'))#于佳琪