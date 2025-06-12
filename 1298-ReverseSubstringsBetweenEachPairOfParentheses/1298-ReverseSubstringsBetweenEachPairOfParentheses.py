# Last updated: 12/6/2025, 5:43:03 am
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                index = stack.pop()
                s = s[0:index+1] + s[index+1:i][::-1] + s[i:]
        
        ret = ''
        for char in s:
            if char != '(' and char != ')': ret += char
        return ret