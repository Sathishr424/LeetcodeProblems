# Last updated: 12/6/2025, 5:51:23 am
class Solution:
    def calculate(self, s: str) -> int:
        stack = deque([])
        curr = 0
        def process(x):
            if len(stack) == 0: return stack.append(x)
            if stack[-1] == '/':
                stack.pop()
                y = stack.pop()
                stack.append(y//x)
            elif stack[-1] == '*':
                stack.pop()
                y = stack.pop()
                stack.append(x*y)
            else:
                return stack.append(x)
        for num in s:
            if num not in "+/-*":
                if num != ' ': curr = curr * 10 + int(num)
            else:
                process(curr)
                stack.append(num)
                curr = 0
        process(curr)
        ans = 0
        while len(stack) > 1:
            x = stack.popleft()
            o = stack.popleft()
            y = stack.popleft()
            if o == '-':
                stack.appendleft(x-y)
            elif o == '+':
                stack.appendleft(x+y)
        return stack[0]