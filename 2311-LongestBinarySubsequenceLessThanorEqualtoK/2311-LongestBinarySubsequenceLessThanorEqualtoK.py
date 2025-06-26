# Last updated: 26/6/2025, 6:31:38 am
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        curr = 0
        power = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                curr = (1 << power) + curr
                if curr > k:
                    zero = 0
                    for j in range(i):
                        if s[j] == '0': zero += 1
                    return zero + (n - i - 1)
            power += 1
            # print(s[i], i, (curr, power))
        
        return n