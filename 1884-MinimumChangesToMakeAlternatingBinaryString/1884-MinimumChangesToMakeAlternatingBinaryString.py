# Last updated: 12/6/2025, 5:39:59 am
class Solution:
    def minOperations(self, s: str) -> int:
        prev = '0'
        f_ret = 0

        f_ret += s[0] == '1'

        for i in range(1, len(s)):
            if prev == '0':
                f_ret += s[i] == '0'
                prev = '1'
            else:
                f_ret += s[i] == '1'
                prev = '0'
        
        return min(f_ret, len(s) - f_ret)
        
