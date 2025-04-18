# Last updated: 18/4/2025, 3:37:37 pm
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

        start = k
        for i in range(k):
            if stack[i] != '0':
                start = i
                break
        
        return ''.join(stack[start:k]) if k-start else '0'
        