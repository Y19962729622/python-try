# 今天文档的**核心 2h**
# 1. 数值计算案例：素数判断函数，测 2、9、17、100
# 2. 最大公约数 gcd，两种写法：循环版、递归版
# 3. 多返回值，理解 return 返回元组、接收多个结果
# 4. 练习：阶乘函数 + 参数校验，负数直接抛提示

# 例子1：随机验证码
#题目要求：设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。
# import random
# import string
# All_chars=string.ascii_letters+string.digits+string.punctuation
# def generate(code_len=5):
#     '''
#     生成制定长度的验证码
#     :param code_len：验证码的长度（默认为5个字符）
#     :return: 生成随机由数字、大小写字母生成的5为验证码
#     '''
#     return ''.join(random.choices(All_chars,k=code_len))
# print(generate(code_len=5))

# import random
# import string
# #定义一个变量存储要求的验证码数据类型。
# ALL_CHARS=string.digits+string.ascii_letters
# def generate(*,code_len=6):
#     '''
#     生成一个6位字符的验证码
#     :param code_len: 验证码长度为6位
#     :return: 输出一个长度为6位的包含数字、大小写字母的验证码
#     '''
# #random.choices从变量中随机挑选字符，但此时还是无序的，然后再用''.join拼接成列表。
#     return ''.join(random.choices(ALL_CHARS,k=code_len))
# print(generate(code_len=6))

# 例子2:判断素数
# 要求：设计一个判断给定的大于1的正整数是不是质数的函数。
# 质数是只能被1和自身整除的正整数（大于1），如果一个大于1的正整数N是质数，
# 那就意味着在2到N-1之间都没有它的因子。
# num=int(input('n='))
# def is_prime(n):
#     for i in range(2,n):
#         if n//i!=0:
#             return False
#         else:
#             return True

# def is_prime(n)->bool:
#     for i in range(2,int(n**2)+1):
#         if n%i==0:
#             return False
#     return True

# 例子3：最大公约数和最小公倍数
# 设计计算两个正整数最大公约数和最小公倍数的函数。
# x和y的最大公约数是能够同时整除x和y的最大整数，
# 如果x和y互质，那么它们的最大公约数为 1；x和y的最小公倍数是能够同时被x和y整除的最小正整数，
# 如果x和y互质，那么它们的最小公倍数为x×y 。
# 需要提醒大家注意的是，计算最大公约数和最小公倍数是两个不同的功能，应该设计成两个函数，
# 而不是把两个功能放到同一个函数中。
#递归版
# def gcd(x,y):
#     d=min(x,y)
#     for i in range(d,1,-1):
#         if x%i==0 and y%i==0:
#             return i
#     return 1
# def lcm(x,y):
#     return x*y/gcd(x,y)
# print(lcm(4,8))

# def gcd(a,b):
#     d=min(a,b)
#     for i in range(d,1,-1):
#         if a%i==0 and b%i==0:
#             return i
#     return 1
# def lcm(a,b):
#     return a*b//gcd(a,b)
# print(lcm(6,9))

#取余版
# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)
# print(gcd(30,100))

#专练
# 写函数 `calc(n)`，接收一个正整数 n。
# 函数要同时算出两个结果：
# 1. 1～n 所有整数的**总和**
# 2. 1～n 所有整数的平方和
# 把这两个结果打包成元组返回。
# 示例：
# `calc(3)`
# 总和 = 1+2+3 = 6
# 平方和 = 1+4+9 = 14
# 返回 `(6, 14)`
# def calc(n):
#     sum_total=0
#     sum_sq=0
#     for i in range(1,n+1):
#          sum_total+=i;sum_sq+=i**2
#     return (sum_total,sum_sq)
# print(calc(5))

# 题目：写函数 `get_stats(lst)`，接收一个全部是正整数的列表。
# 函数需要算出：
# 1. 列表里面的最大值
# 2. 列表里面的最小值
# 打包成元组返回。
# 例子：
# `get_stats([5,2,9,1,7])` → 返回 `(9, 1)`

# def get_stats(lst):
#     for _ in lst:
#         a=max(lst)
#         b=min(lst)
#     return (a,b)
# print(get_stats([1,2,3,4,5]))

# 题目
# 写函数 factorial(n: int) -> int，计算 n 的阶乘。
# 要求：
# 阶乘定义：
# n!=1×2×⋯×n;规定 0!=1
# 参数校验：如果传入的 n < 0，打印提示文字 "负数没有阶乘"，并且返回 None
# n 是 0 或者正整数时，正常算出阶乘返回整数
# 示例：
# factorial(4) → 24
# factorial(0) → 1
# factorial (-5) → 打印提示，返回 None

# def factorial(n:int)->int:
#     if n<0:
#         print('负数没有阶乘')
#         return None
#     res=1
#     for i in range(1,n+1):
#         res*=i
#     return res
# print(factorial(4))
#错的地方
#   return factorial(n)
# print(factorial(5))

# 专练——题目：
# 写函数 `power_calc(base: int, exp: int) -> int`，计算 base 的 exp 次幂（base^exp）
# 要求：
# 1. exp 是**非负整数**
# 2. 参数校验：如果 exp < 0，打印 `暂不支持负指数`，返回 None
# 3. 不用 `**` 运算符，用循环相乘实现
# 4. 规定：任何数的 0 次幂结果是 1
# 示例：
# power_calc (2,3) → 8
# power_calc (5,0) → 1
# power_calc (3,-2) → 打印提示，返回 None
def power_calc(base:int,exp:int)->int:
    new_base=1
    if exp<0:
        print('暂不支持负指数')
        return None
    for _ in range(exp):
        new_base*=base
    return new_base
print(power_calc(3,-2))



