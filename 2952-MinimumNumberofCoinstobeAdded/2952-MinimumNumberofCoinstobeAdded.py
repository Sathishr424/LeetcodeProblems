# Last updated: 9/5/2025, 2:42:32 pm
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [[-1] * target for _ in range(n)]
        
        def rec(index, total):
            if total == target: return 0
            elif total > target or index == n: return -float('inf')
            elif dp[index][total] != -1: return dp[index][total]
            
            ans = max(rec(index+1, total+nums[index]) + 1, rec(index+1, total))
        
            dp[index][total] = ans
            return ans
        
        ret = rec(0, 0)
        if ret == -float('inf'): return -1
        return ret

