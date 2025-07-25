# Last updated: 25/7/2025, 9:30:21 pm
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)

        stack = []
        i = 0
        while i < n:
            if s[i] == '+':
                stack.append('+')
            elif s[i] == '-':
                stack.append('-')
            elif s[i] == '*':
                stack.append('*')
            elif s[i] == '/':
                stack.append('/')
            elif s[i] != ' ':
                curr = 0
                while i < n and s[i] in '0123456789':
                    curr = curr * 10 + int(s[i])
                    i += 1
                if stack:
                    if stack[-1] == '*':
                        stack.pop()
                        stack[-1] *= curr
                    elif stack[-1] == '/':
                        stack.pop()
                        stack[-1] //= curr
                    else:
                        stack.append(curr)
                else: 
                    stack.append(curr)
                continue
            i += 1
        
        ret = stack[0]
        for i in range(1, len(stack)):
            if stack[i] != '+' and stack[i] != '-':
                if stack[i-1] == '+': ret += stack[i]
                else: ret -= stack[i]

        return ret
