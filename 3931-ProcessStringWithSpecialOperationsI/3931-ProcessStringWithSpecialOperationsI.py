# Last updated: 12/25/2025, 7:10:39 PM
class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '#':
                stack += stack
            elif char == '*':
                if stack: stack.pop()
            elif char == '%':
                stack = stack[::-1]
            else:
                stack.append(char)

        return ''.join(stack)