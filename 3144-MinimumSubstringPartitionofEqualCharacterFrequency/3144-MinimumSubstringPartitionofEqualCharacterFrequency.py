# Last updated: 7/7/2025, 9:14:16 pm
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        inf = float('inf')
        def charToInt(a):
            return ord(a) - ord('a')
        
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for index in range(n):
            freq = [0] * 26
            max_freq = 0
            cnt = 0

            for i in range(index, n):
                a = charToInt(s[i])
                freq[a] += 1
                if freq[a] == 1: cnt += 1
                if freq[a] > max_freq:
                    max_freq += 1
                if max_freq * cnt == (i - index + 1):
                    dp[i + 1] = min(dp[index] + 1, dp[i+1])

        return dp[-1]