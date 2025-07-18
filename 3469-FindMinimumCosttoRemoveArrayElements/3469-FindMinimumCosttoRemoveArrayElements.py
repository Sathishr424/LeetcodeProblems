# Last updated: 18/7/2025, 2:40:43 pm
cmax = lambda x, y: x if x > y else y

class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [[-1] * (n + 1) for _ in range(n)]

        def rec(x, y):
            if dp[x][y] != -1: return dp[x][y]
            z = y + 1
            if  y >= n or z >= n:
                curr = nums[x]
                if y < n and nums[y] > curr: 
                    curr = nums[y]
                if z < n and nums[z] > curr: 
                    curr = nums[z]
                return curr
            one = rec(z, z + 1) + cmax(nums[x], nums[y])
            two = rec(y, z + 1) + cmax(nums[x], nums[z])
            three = rec(x, z + 1) + cmax(nums[y], nums[z])
            dp[x][y] = min(one, two, three)
            return dp[x][y]
        
        return rec(0, 1)