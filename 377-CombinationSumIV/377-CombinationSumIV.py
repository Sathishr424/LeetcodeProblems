# Last updated: 9/5/2025, 7:52:03 pm
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target+1) 
        dp[0] = 1

        for i in range(target):
            for num in nums:
                if num+i > target: break
                dp[num+i] += dp[i]
        
        return dp[target]