# Last updated: 25/4/2025, 1:08:10 am
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        base = 28
        mod = 10 ** 9 + 7

        left = 0
        right = 0
        ret = 0

        for i in range(n-1):
            index_left = ord(s[i]) - 96
            index_right = ord(s[n-i-1]) - 96

            left = ((left * base % mod) + index_left) % mod
            right = (right + (index_right * pow(base, i, mod) % mod)) % mod

            if left == right: ret = i+1
        
        return s[:ret]