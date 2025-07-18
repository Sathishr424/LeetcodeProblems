# Last updated: 18/7/2025, 2:36:50 pm
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n)]

        def rec(x, y):
            if dp[x][y] != -1: return dp[x][y]
            z = y + 1
            if  y >= n or z >= n:
                curr = nums[x]
                if y < n: curr = max(curr, nums[y])
                if z < n: curr = max(curr, nums[z])
                return curr
            one = rec(z, z + 1) + max(nums[x], nums[y])
            two = rec(y, z + 1) + max(nums[x], nums[z])
            three = rec(x, z + 1) + max(nums[y], nums[z])
            dp[x][y] = min(one, two, three)
            return dp[x][y]
        
        return rec(0, 1)