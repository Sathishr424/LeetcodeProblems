# Last updated: 9/5/2025, 3:18:55 pm
cmax = lambda x, y: x if x > y else y
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [[-float('inf')] * (target+1) for _ in range(n+1)]
        dp[0][0] = 0

        ans = -float('inf')
        
        for i in range(1, n+1):
            num = nums[i-1]
            for t in range(target):
                if t+num > target: break
                dp[i][t] = cmax(dp[i-1][t], dp[i][t])
                dp[i][t+num] = cmax(dp[i-1][t+num], dp[i-1][t] + 1)
            ans = cmax(ans, dp[i][target])
                    
        return ans if ans != -float('inf') else -1
