# Last updated: 9/4/2025, 5:59:13 pm
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k >= n: return '0'
        k = n - k
        stack = []
        for i, char in enumerate(num):
            exit_ = False
            while stack and ord(stack[-1]) > ord(char):
                if len(stack) + (n-i) <= k:
                    exit_ = True
                    break
                stack.pop()
            
            stack.append(char)
            if exit_: break
        
        st = ''.join(stack[:k]) + num[i+1:]
        for i in range(k):
            if st[i] != '0': return st[i:]
        
        return '0'
