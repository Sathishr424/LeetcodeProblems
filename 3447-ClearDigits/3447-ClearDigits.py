# Last updated: 12/6/2025, 5:35:36 am
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for char in s:
            if char.isdigit():
                if stack: stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)