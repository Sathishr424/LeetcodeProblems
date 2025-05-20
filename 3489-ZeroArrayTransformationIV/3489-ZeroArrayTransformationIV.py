# Last updated: 20/5/2025, 3:22:10 pm
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)
        m = len(queries)
        maxi = max(nums)

        dp = [[[-1] * n for _ in range(maxi+1)] for _ in range(m)]
        
        def rec(index, need, k):
            if need == 0: return k-1
            if k == m: return m
            if dp[k][need][index] != -1: return dp[k][need][index]

            ans = rec(index, need, k+1)
            x, y, val = queries[k]
            if x <= index and y >= index and need - val >= 0:
                ans = min(ans, rec(index, need-val, k+1))
            dp[k][need][index] = ans
            return ans
        
        ret = -1
        for i, num in enumerate(nums):
            if num == 0: continue
            ret = max(ret, rec(i, num, 0))
        
        return -1 if ret >= m else ret+1
            


