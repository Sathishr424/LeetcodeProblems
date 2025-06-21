# Last updated: 21/6/2025, 9:25:09 am
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = [0] * 26
        for char in word:
            freq[ord(char) - 97] += 1

        arr = sorted([freq[i] for i in range(26) if freq[i]])
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def rec(l, r):
            # if dp[l][r] != -1: return dp[l][r]
            if l == r: return 0

            diff = arr[r] - arr[l]
            if diff > k:
                dp[l][r] = min(rec(l+1, r) + arr[l], rec(l, r-1) + diff - k)
            else:
                dp[l][r] = 0
            return dp[l][r]
        
        return rec(0, n-1)