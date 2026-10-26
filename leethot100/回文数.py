class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
if __name__ == "__main__":#（测试语句）
   try:
    user_input=input('请输入一个整数：')
    x=int(user_input)
    print(f'user_input')
    result=Solution().isPalindrome(x)
    print(f'{x}是一个回文数'if result else f'{x}不是一个回文数')
   except ValueError:
       print('这不是一个有效数字')


