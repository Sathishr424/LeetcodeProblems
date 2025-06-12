# Last updated: 12/6/2025, 5:55:05 am
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = 0
        for char in s:
            if char == ')':
                if not stack or stack.pop() != '(': return False
                open -= 1
            elif char == ']':
                if not stack or stack.pop() != '[': return False
                open -= 1
            elif char == '}':
                if not stack or stack.pop() != '{': return False
                open -= 1
            else:
                open += 1
                stack.append(char)
        return open == 0