# Last updated: 15/5/2025, 1:46:36 am
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        dp = [[-1] * n for _ in range(n)]

        def process(i, j):
            if dp[i][j] != -1: return dp[i][j]
            prev = arr[i]
            curr = arr[j]
            num = curr - prev
            if prev > num and num in added:
                dp[i][j] = process(added[num], i) + 1
            else:
                dp[i][j] = 0
            return dp[i][j]
        
        ret = 0
        added = {}
        for i in range(n):
            for j in range(i+1, n):
                ans = process(i, j)
                if ans > 0:
                    ret = max(ret, ans + 2)
                        
            added[arr[i]] = i
        
        return ret
