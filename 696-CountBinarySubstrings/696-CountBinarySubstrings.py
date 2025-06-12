# Last updated: 12/6/2025, 5:47:35 am
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ret = 0
        ones = int(s[0] == '1')
        zero = int(s[0] == '0')
        prev = s[0]

        for i in range(1, len(s)):
            if s[i] != prev:
                ret += min(zero, ones)
                if prev == '0': ones = 0
                else: zero = 0
            
            if s[i] == '0': zero += 1
            else: ones += 1
            prev = s[i]

        return ret + min(zero, ones)

        