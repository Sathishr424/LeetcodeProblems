# Last updated: 12/6/2025, 5:33:23 am
class Solution:
    def resultingString(self, s: str) -> str:
        n = len(s)

        stack = []
        
        for i, char in enumerate(s):
            curr = ord(char) - 97
            if stack and ((stack[-1] + 1) % 26 == curr or (stack[-1] - 1) % 26 == curr):
                stack.pop()
            else:
                stack.append(curr)

        return ''.join([chr(char + 97) for char in stack])