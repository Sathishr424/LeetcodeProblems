# Last updated: 21/7/2025, 11:42:52 am
class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for char in s:
            if len(stack) > 1 and stack[-2] == stack[-1] and stack[-1] == char:
                stack.pop()
            stack.append(char)
        
        return ''.join(stack)