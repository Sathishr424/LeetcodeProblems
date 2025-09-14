# Last updated: 15/9/2025, 5:09:10 am
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)

        indexes = [-1] * 26
        cnt = 0
        for i in range(n):
            a = ord(s[i]) - ord('a')
            left = indexes[a] + 1
            
            cnt += (n - i) * (i - left + 1)
            indexes[a] = i

        return cnt
