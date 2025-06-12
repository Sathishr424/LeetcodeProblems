# Last updated: 12/6/2025, 5:43:57 am
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        
        return "".join(stack)