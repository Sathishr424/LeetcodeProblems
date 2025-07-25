# Last updated: 25/7/2025, 6:38:51 pm
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0
        for i in range(n):
            freq = defaultdict(int)
            for j in range(i, n):
                freq[s[j]] += 1
                if freq[s[j]] == k:
                    ret += n - j
                    break
        
        return ret
