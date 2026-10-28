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

# 给定列表 `words = ["hi", "", "python", "", "ok", ""]`
# 使用 `filter` 去掉里面的空字符串，保留有效字符串。
# 预期输出：`['hi', 'python', 'ok']`
def string(x):
    return x != ""


words = ["hi", "", "python", "", "ok", ""]
res = list(filter(string, words))
print(res)  # ['hi', 'python', 'ok']

# TODO 明天补：reduce（from functools import reduce）
