# Last updated: 25/7/2025, 6:40:46 pm
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                a = ord(s[j]) - ord('a')
                freq[a] += 1
                if freq[a] == k:
                    ret += n - j
                    break
        
        return ret
