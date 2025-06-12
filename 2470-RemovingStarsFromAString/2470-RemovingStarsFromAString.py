# Last updated: 12/6/2025, 5:37:57 am
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)