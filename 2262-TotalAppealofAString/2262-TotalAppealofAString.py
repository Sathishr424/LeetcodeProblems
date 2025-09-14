# Last updated: 15/9/2025, 5:08:17 am
class Solution:
    def appealSum(self, s: str) -> int:
        # s = [chr(random.randrange(26) + ord('a')) for _ in range(10 ** 5)]
        n = len(s)

        indexes = {}
        cnt = 0
        for i in range(n):
            left = 0 if s[i] not in indexes else indexes[s[i]] + 1
            
            cnt += (n - i) * (i - left + 1)
            indexes[s[i]] = i

        return cnt
