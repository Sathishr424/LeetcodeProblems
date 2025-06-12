# Last updated: 12/6/2025, 5:35:30 am
class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        prev = n
        ones = 0
        op = 0

        for i in range(n):
            if s[i] == '1':
                prev = i
                ones += 1
                break
        
        for i in range(prev+1, n):
            if s[i] == '1':
                if i - prev > 1:
                    op += ones
                prev = i
                ones += 1
        
        if s[-1] == '0': return op+ones
        return op
                    