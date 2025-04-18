# Last updated: 18/4/2025, 3:33:37 pm
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        k = n-k

        stack = []
        for i, char in enumerate(num):
            while stack and stack[-1] > char:
                if len(stack) + (n-i) == k: break
                stack.pop()
            
            stack.append(char)

        ret = ''
        for char in stack[:k]:
            if ret or char != '0': ret += char
        
        return ret if ret else '0'
        