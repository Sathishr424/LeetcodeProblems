# Last updated: 18/4/2025, 3:41:37 pm
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        k = n-k

        stack = []
        def helper():
            for i, char in enumerate(num):
                while stack and stack[-1] > char:
                    if len(stack) + (n-i) == k: return i
                    stack.pop()
                
                stack.append(char)
            return n
        index = helper()
        for i in range(index, n): stack.append(num[i])
        start = k
        for i in range(k):
            if stack[i] != '0':
                start = i
                break
        
        return ''.join(stack[start:k]) if k-start else '0'
        