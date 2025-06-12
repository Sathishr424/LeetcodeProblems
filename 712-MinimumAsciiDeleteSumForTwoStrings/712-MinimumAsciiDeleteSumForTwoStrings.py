# Last updated: 12/6/2025, 5:47:31 am
alp = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122}

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        tot = 0
        for s in s1:
            tot += alp[s]
        for s in s2:
            tot += alp[s]
        dp = [[tot for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] - (alp[s1[i-1]] * 2)
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
        