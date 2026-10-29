# def calc(*args,**kwargs):
#     '''
#     *args:接受任意多个位置参数，打包成元组
#     **kwargs:接受任意多个关键字参数，打包成字典
#     这个函数实现的功能传入任意多个参数，数量不限
#     '''
#     items=list(args)+list(kwargs.values())
#     #list(args)把元组转化成列表，list(kwargs.values())只要字典里的值，不要关键字，并打包成数组
#     result=0 #定义初始变量，当作容器用来封装结果
#     for item in items:
#         if type(item) in(int,float):#注意这步的写法，判断参数类型，它用的是if……in……
#             result+=item
#     return result

#高阶函数用法，功能添加：实现更多的甚至是自定义的二元运算
# def calc(init_value,op_func,*args,**kwargs):
#     '''
#     :param init_value: 函数运算的起点为自定义，之前是默认为0，如果出现乘法就没法算
#     :param op_func:是一个函数，接收函数作为参数，就是要学的高阶函数
#     :return:将传进来的参数按照指定的运算过程进行运算输出
#     '''
#     items=list(args)+list(kwargs.values())
#     result=init_value
#     for item in items:
#         if type(item) in (int,float):
#             result=op_func(result,item)#将初值，与传进来的参数按照op_func进行运算
#     return result
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print(calc(7,mul,2,3,4,5))

#练习map:
# def tru(x):
#     return x*3
# nums=[2,3,4,5]
# res=list(map(tru,nums))
# print(res)

#练习filter:
#失误版
# def is_zheng(x):
#     if x>0:
#         return True
#     else:
#         return False
# nums=[2,-5,10,-3,8,-1]
# res=filter(is_zheng,nums)
# print(res)
#1.函数的结果本身就是布尔值，可以简写，直接return>0就行，
#2.filter返回的是迭代器对象，看不到里面的元素，想查看内容必须套list()

# def is_zheng(x):
#     return x>0
#
# nums=[2,-5,10,-3,8,-1]
# res=list(filter(is_zheng,nums))
# print(res)

#练习：map+filter组合题
# 列表 `scores = [88, 59, 92, 45, 76, 66]`
# 要求：先用 filter 筛选出大于等于 60 的及格分数，再用 map 把及格分数 +5 分，转列表打印。
# 预期输出：`[93, 97, 81, 71]`
# def right_score(x):
#     return x>=60
#
# def add_score(x):
#      x+=5
#      return x
#
# scores=[88,59,92,45,76,66]
# first=list(filter(right_score,scores))
# res=list(map(add_score,filter(right_score,scores)))
# print(first) #[88, 92, 76, 66]
# print(res)   #[93, 97, 81, 71]

#基本上可以跑，还是那个问题，return 可以直接跑条件，第一个长记性了，但第二个没长记性！

# def right_score(x):
#     return x>=60
#
# def add_score(x):
#      return x+5
#
# scores=[88,59,92,45,76,66]
# first=list(filter(right_score,scores))
# res=list(map(add_score,filter(right_score,scores)))
# print(first) #[88, 92, 76, 66]
# print(res)   #[93, 97, 81, 71]

# 文档练习题：
# 要去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表，
# def is_even(x):
#     return x%2==0
#
# def square(x):
#     return x**2
#
# nums=[35, 12, 8, 99, 60, 52]
# res=list(map(square,(filter(is_even,nums))))
# print(res)

#sorted函数
#题目1
# nums=[9,2,7,1,5]
# sortednums=sorted(nums,reverse=True)
# print(sortednums)

#题目2
# fruits = ["pear", "watermelon", "apple", "banana"]
# new_fruits=sorted(fruits,key=len)
# print(new_fruits)

# #进阶题
# stu = [("张三", 82), ("李四", 95), ("王五", 78)]
# scores=sorted(stu,key=lambda x:x[1])
# print

#关于lambda练习题
#1、sorted+lambda
# animal = [("cat", 3), ("dog", 1), ("bird", 2)]
# nums=sorted(animal,key=lambda x:x[1])
# print(nums)

#2、map+lambda
# def triple(x):
#     return x*3
# nums = [1, 3, 5, 7]
# new_nums=list(map(triple,nums))
# print(new_nums)

# nums = [1, 3, 5, 7]
# new_nums=list(map(lambda x:x*3,nums))
# print(new_nums)

#3、filter+lambda
# nums = [2, 5, 8, 11, 14, 17]
# new_nums =list(filter(lambda x:x>10,nums))
# print(new_nums)

#综合题、sorted + map + filter + lambda
# 需求步骤：
# 1. 使用 `filter + lambda`：过滤掉名字为空字符串的学生
# 2. 使用 `map + lambda`：把每个人的分数加 5 分
# 3. 使用 `sorted + lambda`：按照加分后的分数从高到低排序
# 4. 最后输出最终列表

# students = [("Tom", 66), ("Jack", 80), ("", 55), ("Rose", 91), ("Mike", 72), ("Lily", 48)]
# new_list =list(sorted(
#     map(lambda x:(x[0],x[1]+5),filter(lambda x:x[0]!="",students)),key=lambda x:x[1],reverse=True))
# print(new_list)

#reduce函数练习题：reduce+lambda
from functools import reduce
# nums = [3,4,5,6]
# result=reduce(lambda x,y:x*y,nums)
# print(result)

#reduce综合题：filter + map + reduce + lambda
# 要求：
# 1. filter：筛选出偶数
# 2. map：每个偶数 + 1
# 3. reduce：把处理完的数字全部相乘 写出代码。

# data = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# answer=reduce(lambda x ,y:x*y,map(lambda x:x+1,filter(lambda x:x%2==0,data)))
# print(answer)

#lambda判断素数
# is_prime=lambda x:all(map(lambda f:x%f,range(1,int(x**0.5)+1)))
# print(is_prime(10))

#偏函数functools
from functools import partial
# def mul(a,b):
#     return a*b
# mul5 = partial(mul, 5)
# print(mul5(3))

#题目1
# 要求：利用 partial 创建偏函数 `sub10`，固定 `a=10`，调用 `sub10(3)` 输出 7。
from functools import partial
# def calc(a, b):
#     return a - b
# sub10=partial(calc,10)
# print(sub10(3))

# 题目2
# 要求：reduce + lambda，计算列表所有数字相乘的结果。
# nums = [2,4,6,8]
# result= reduce(lambda x,y:x*y,nums)
# print(result)

#题目3
def power(base,exp):
    return base**exp
lst=[1,2,3,4]
cube_func=partial(power,exp=3)
cube=list(map(cube_func,lst))
print(cube)