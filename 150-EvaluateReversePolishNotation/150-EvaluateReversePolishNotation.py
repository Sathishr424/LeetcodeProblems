# Last updated: 12/6/2025, 5:52:19 am
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tmp = {'+': 1, '-': 1, '/': 1, '*': 1}
        for t in tokens:
            if t not in tmp:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                if t == '+':
                    stack.append(x+y)
                elif t == '-':
                    stack.append(x-y)
                elif t == '*':
                    stack.append(x*y)
                elif t == '/':
                    stack.append(int(x/y))
        return stack[0]