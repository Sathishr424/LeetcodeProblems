# Last updated: 6/4/2025, 9:59:39 pm
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        dp = {}
        ret = []
        nums.sort()

        for i in range(n-1, -1, -1):
            dp[nums[i]] = []
            for j in range(i+1, n):
                if nums[j] % nums[i]  == 0 and len(dp[nums[j]]) > len(dp[nums[i]]):
                    dp[nums[i]] = dp[nums[j]]
                
            dp[nums[i]] = [nums[i]] + dp[nums[i]]
            
            if len(dp[nums[i]]) > len(ret):
                ret = dp[nums[i]]

        return ret

