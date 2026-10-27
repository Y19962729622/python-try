# set1={1,2,2,3,3,3,4,4,4,4}
# # print(set1)#{1, 2, 3, 4}
# set2={'apple','banana','orange','lemon','grape','mango'}
# print(set2)
# print(set2)#{'banana', 'orange', 'apple'}
# set3=set('green')
# print(set3)#{'r', 'g', 'e', 'n'}
# set4=set(['apple','banana','orange'])
# print(set4)#{'banana', 'orange', 'apple'}
# set5={num for num in range(1,30) if num%4==0 and num%6==0}
# print(set5) #{24, 12}
# print(len(set1)) #4

# for i in set2:
#     print(i)#grape banana lemon apple orange mango

# print(5 in set2) #False
# print('banana' not in set2) #False

# set3={1,3,5,4,7,8,2}
# set4={2,4,6,8,1,3}
# #交集
# print(set3&set4) #{1, 2, 3, 4, 8}
# print(set3.intersection(set4)) #{1, 2, 3, 4, 8}
# #并集
# print(set3|set4) #{1, 2, 3, 4, 5, 6, 7, 8}
# print(set3.union(set4)) #{1, 2, 3, 4, 5, 6, 7, 8}
# #差集
# print(set3-set4)#{5, 7}
# print(set3.difference(set4)) #{5, 7}
# #对称差,两个集合去掉交集后各自剩余的部分的并集
# print(set3^set4)#{5, 6, 7}
# print(set3.symmetric_difference(set4))#{5, 6, 7}
# set3|=set4
# print(set3)
# #set3.update(set4)
# set5={7,10,34,2,8,6,7}
# set3&=set5 #{1, 2, 3, 4, 5, 6, 7, 8}
# #set3.intersection_update(set5)
# print(set3) #{8, 2, 6, 7}
# set4-=set5
# #set4.difference_update(set5)
# print(set4) #{1, 3, 4}
# set1={1,2,3,4,5}
# set2={2,3,5,7}
# set3={4,3,2}
# print(set3<=set1) #True 3是1的子集
# print(set2<set1)  #False 2是1的子集
# print(set2.issubset(set3))   #False 2是3的子集
# print(set1.issuperset(set3)) #True  1是3的超集

#添加
# set1.add(6)
# set1.add(10)
# print(set1) #{1, 2, 3, 4, 5, 6, 10}
# #删除
# set1.discard(10)
# print(set1) #{1, 2, 3, 4, 5, 6}
# if 2 in set1:
#     set1.remove(2)
# print(set1) #{1, 3, 4, 5, 6}
# #清除
# set1.clear()
# print(set1) #set()
set1={'green','orange','red','blue'}
set2={'orange','apple','lemon'}
print(set1.isdisjoint(set2)) #False