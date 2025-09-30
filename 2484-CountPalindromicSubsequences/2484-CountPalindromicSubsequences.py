# Last updated: 30/9/2025, 7:55:12 pm
class Solution:
    def countPalindromes(self, s: str) -> int:
        mod = 10**9 + 7
        
        n = len(s)
        s = [int(a) for a in s]
        prefix_reverse = [[0] * 10 for _ in range(n + 1)]
        prefix = [[0] * 10 for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            a = s[i]
            for j in range(10):
                prefix_reverse[i][j] += prefix_reverse[i + 1][j]
            prefix_reverse[i][a] += 1

        prefix[0][s[i]] += 1
        for i in range(1, n):
            a = s[i]
            for j in range(10):
                prefix[i][j] += prefix[i - 1][j]
            prefix[i][a] += 1

        dp = [[-1] * 100 for _ in range(n)]
        dp_reverse = [[-1] * 100 for _ in range(n)]

        def recReverse(index, a, b):
            if index == 0: return 0
            if dp_reverse[index][a * 10 + b] != -1:
                return dp_reverse[index][a * 10 + b]

            ans = recReverse(index - 1, a, b)
            if s[index] == b:
                ans += prefix[index - 1][a]

            ans %= mod
            dp_reverse[index][a * 10 + b] = ans
            return ans

        def rec(index, a, b):
            if index == n - 1: return 0
            if dp[index][a * 10 + b] != -1:
                return dp[index][a * 10 + b]

            ans = rec(index + 1, a, b)
            if s[index] == a:
                ans += prefix_reverse[index + 1][b]

            ans %= mod
            dp[index][a * 10 + b] = ans
            return ans

        ans = 0
        for index in range(2, n-3+1):
            for i in range(10):
                for j in range(10):
                    left = recReverse(index - 1, i, j)
                    right = rec(index + 1, j, i)
                    ans += (left * right) % mod
                    ans %= mod

        return ans