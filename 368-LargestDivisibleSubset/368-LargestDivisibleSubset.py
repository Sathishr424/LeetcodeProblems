# Last updated: 6/4/2025, 10:00:01 pm
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        dp = {}
        ret = []
        nums.sort()

        for i in range(n-1, -1, -1):
            num = nums[i]
            dp[num] = []
            for j in range(i+1, n):
                if nums[j] % num  == 0 and len(dp[nums[j]]) > len(dp[num]):
                    dp[num] = dp[nums[j]]
                
            dp[num] = [num] + dp[num]
            
            if len(dp[num]) > len(ret):
                ret = dp[num]

        return ret

