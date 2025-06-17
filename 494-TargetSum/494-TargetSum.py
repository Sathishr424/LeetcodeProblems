# Last updated: 17/6/2025, 10:45:52 pm
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def rec(index, tot):
            if index == n:
                return 1 if tot == target else 0
            
            ans = rec(index+1, tot + nums[index])
            ans += rec(index+1, tot - nums[index])
            return ans
        
        return rec(0, 0)