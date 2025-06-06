# Last updated: 6/6/2025, 1:20:22 pm
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_char = [''] * n
        min_char[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_char[i] = min(s[i], min_char[i + 1])
        
        t = []
        res = []
        i = 0
        while i < n:
            t.append(s[i])
            while t and (i == n - 1 or min_char[i + 1] >= t[-1]):
                res.append(t.pop())
            i += 1
        
        return ''.join(res)
