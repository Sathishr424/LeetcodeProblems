# Last updated: 25/6/2025, 9:21:01 am
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)