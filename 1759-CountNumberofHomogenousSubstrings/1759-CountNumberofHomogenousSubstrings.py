# Last updated: 16/4/2025, 5:57:16 pm
mod = 10**9 + 7

class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        
        ret = 0
        prev = ''
        cnt = 1

        for i, char in enumerate(s):
            if char == prev:
                cnt += 1
            else:
                cnt = 1
            prev = char
            ret = (ret + cnt) % mod

        return ret