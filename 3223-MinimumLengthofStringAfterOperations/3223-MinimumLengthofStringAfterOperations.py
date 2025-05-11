# Last updated: 11/5/2025, 10:28:40 am
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = [0] * 26

        for char in s:
            freq[ord(char) - 97] += 1
        
        ret = 0
        for i in range(26):
            cnt = freq[i]
            while cnt >= 3:
                cnt -= 2
            ret += cnt
        
        return ret