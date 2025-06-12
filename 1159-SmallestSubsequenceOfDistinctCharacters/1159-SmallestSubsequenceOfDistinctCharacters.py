# Last updated: 12/6/2025, 5:43:51 am
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)

        indexes = {}
        for i, char in enumerate(s): indexes[char] = i

        stack = []
        seen = {}
        
        for i, char in enumerate(s):
            if char in seen: continue
            
            while stack and stack[-1] > char:
                if indexes[stack[-1]] < i: break
                del seen[stack.pop()]
            
            seen[char] = 1
            stack.append(char)
        
        return ''.join(stack)

        