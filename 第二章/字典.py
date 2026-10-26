# lesson={'MON':'有一节课在早八','TUS':'周二的课分单双周，这周是双周，要去上课','WES':'周三原来没有课，被调了一节到上午'}
# print(lesson) #{'MON': '有一节课在早八', 'TUS': '周二的课分单双周，这周是双周，要去上课', 'WES': '周三原来没有课，被调了一节到上午'}
# print(lesson['MON'])#有一节课在早八
# print(lesson['TUS'])#周二的课分单双周，这周是双周，要去上课


# person=dict(name='王五',age='24',home='A市A区A街道A路A小区',work='低调的房地产老板')
# print(len(person)) #{'name': '王五', 'age': '24', 'home': 'A市A区A街道A路A小区', 'work': '低调的房地产老板'}
# #通过内置函数zip压缩序列并创建字典
# item1=dict(zip('ABCDE','12345'))#{'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
# item2=dict(zip('FGHIJ',range(10)))#{'F': 0, 'G': 1, 'H': 2, 'I': 3, 'J': 4}
# print(item1)
# print(item2)
# #字典生成式语法创建字典
# item3={x:x**2 for x in range(10) if x%2==0}
# print(item3) #{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# for key,value in person.items():
#     print(key,value)#name 王五 age 24 home A市A区A街道A路A小区 work 低调的房地产老板
# person={'name':'王五',
#         'age':'24',
#         'home':'A市A区A街道A路A小区',
#         'family':['已婚，有小孩,小孩刚出生不久','父母退休教师，现全球旅居'],
#         'work':'房地产老板',
#         'money':{
#                'company':'旗下拥有一家上市公司',
#                'house':'M国市中心有一套写字楼',
#                'others':'在大西洋拥有一个私人岛屿'
#         }
# }
# print(person)
# #成员运算
# print('plant'in person) #False
# print('work'in person)  #True
# #索引运算
# print(person['home']) #A市A区A街道A路A小区
# person['name']='赵六'
# person['age']='22'
# print(person) #有改动的地方'name': '赵六', 'age': '22',
# #循环遍历
# for i in person:
#     print(f'{i}:\t{person[i]}') #就是把集合里面的元素罗列出来。
# print(person.get('family')) #['已婚，有小孩,小孩刚出生不久', '父母退休教师，现全球旅居']
# print(person.get('love',"你无所爱")) #你无所爱

# school={'name':'南邮通达','place':'江苏省扬州市','student':'about 8000人','origin':'2011年'}
# print(school.keys())  #dict_keys(['name', 'place', 'student'])
# print(school.values())#dict_values(['南邮通达', '江苏省扬州市', 'about 8000人'])
# print(school.items()) #dict_items([('name', '南邮通达'), ('place', '江苏省扬州市'), ('student', 'about 8000人')])
# for keys,values in school.items():
#     print(keys,values)
# name 南邮通达
# place 江苏省扬州市
# student about 8000人

# people={'婴儿':'0-12个月','孩童':'1-7岁','青年':'7-14岁'}
# #school.update(people)
# school|=people
# print(school)

# print(school.pop('name')) #南邮通达
# print(school) #{'place': '江苏省扬州市', 'student': 'about 8000人'}
# print(school.popitem()) #('origin', '2011年')
# print(school) #{'place': '江苏省扬州市', 'student': 'about 8000人'}
# school.clear()
# print(school) #
# del school['name']
# del school['place']
# print(school) #{'student': 'about 8000人', 'origin': '2011年'}


#输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出。统计次数，需要一个容器
# sentence=str(input('请输入一段话：'))
# counter={}
# for ch in sentence:
#     if 'A'<=ch<='Z' or 'a'<=ch<='z':
#         counter[ch]=counter.get(ch,0)+1
# sorted_keys=sorted(counter,key=counter.get,reverse=True)
# for key in sorted_keys:
#     print(f'字母{key}出现了{counter[key]}次.')

#在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
#基础题1
# stu={'姓名':'小李','年龄':'20','专业':'计算机','地址':'扬州'}
# print(stu)
#
# #基础题2
# stu.get('phone',0)
# print(stu.get('phone',0))

#基础题3
#存在时返回20，不存在时返回0

#方法题4
#执行后，字典变成{'a':'10','c':'30'};删除最后一组键值对，也就是键为c的那一组

#方法题5
# d1={'name':'王五','age':'24'}
# d2={'work':'房地产老板','money':'很多'}
# d1.update(d2)
# print(d1)

#方法题6:字典推导式
# stocks={'A公司':80,'B公司':150,'C公司':200,'D公司':60}
# new_stocks={key:value for key,value in stocks.items() if value>100}
# print(new_stocks) #如果对了的话，记得字典推导式里面也要写key:value!

# #综合大题7
# sentence=input('请输入一段话：')
# counter={}
# for ch in sentence:
#     if 'A'<=ch<='Z' and 'a'<=ch<='z':
#         counter['A:Z'] = counter['a:z']
#         counter[ch]=counter.get(ch,0)+1
# sorted_keys=sorted(counter,key=counter.get,reverse=True)
# for k in sorted_keys:
#     print(f'字母{k}出现了{counter[k]}次')


#思考题8
#有问题，sorted第一个参数是按照排序的元素，而counter是一个集合，无法直接给集合排序。

#大题练习
# student = {"name":"张明", "age":19, "major":"计算机", "score":86}
# print(student.get('phone','暂无手机号'))
# extra={'height':175,'score':92}
# student.update(extra)
# print(student)
# print(student.pop('age'))
# for key,value in student.items():
#     print(f'{key}:{value}')
# if 'gender' in student:
#     print('有性别信息')
# else:
#     print('无性别信息')
