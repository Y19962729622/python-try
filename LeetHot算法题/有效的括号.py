# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
class Solution:
    def isValid(self, s: str) -> bool:
        match={'(':')','[':']','{':'}'}
        stack=[] #当作栈
        #遍历列表s里的字符
        for char in s:
            #一个一个判断s字符是不是左括号
            if char in match:
                #如果是的话入栈，出现在列表的最前面，遵循栈的先进后出原则。
                stack.append(char)
            else:
                #如果char不是左括号，而是右括号，先检查栈里面是不是空的，是空的返回False
                if not stack: #如果是空栈
                    return False
                #不是空的，继续这一步，返回栈最顶端的值，也就是列表最前的值，拿出来再通过match匹配
                top=stack.pop()
                if match[top]!=char:
                    return False
        return len(stack)==0
sol=Solution()
print(sol.isValid(s='[(){}]'))
