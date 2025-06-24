# Last updated: 25/6/2025, 12:15:25 am
inf = float('inf')
cmin = lambda x, y: x if x < y else y

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [inf] * n
        dp[0] = 0

        for i in range(n):
            for j in range(nums[i]):
                index = i + j + 1
                if index == n: break
                dp[index] = cmin(dp[index], dp[i] + 1)
        
        return dp[n-1]