# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# （10/27 清理：误留的 pandas 导入已删，本机没装 pandas 会导致文件运行即报错）
# （10/29 修正：return 原先缩进在 while 内只交换一次，现移出 while，整轮跑完再返回）

def solution(s: list[str]):
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


print(solution(["a", "b", "c", "a", "b", "c"]))   # ['c','b','a','c','b','a']
print(solution(["a", "1", "6", "H", "b", "c"]))   # ['c','b','H','6','1','a']

#相关题目练习：题目：
# 写函数 `reverse_only_letter(s: list)`
# 输入：由字符组成的列表，里面包含英文字母和数字。
# 规则：**只把字母原地反转位置，数字留在原地不动**，O (1) 额外空间。
# 不用创建新列表。
# 示例：
# 输入：`['a','1','b','c','2','d']`
# 里面字母依次：a,b,c,d → 反转成 d,c,b,a
# 结果：`['d','1','c','b','2','a']`

def reverse_only_letters(s:list):
    left=0
    right=len(s)-1
    while left<right:
        if not s[left].isalpha():
            left+=1
        elif not s[right].isalpha():
            right-=1
        else:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
    return s


print(reverse_only_letters(['a','1','b','c','2','d']))   # ['d','1','c','b','2','a']