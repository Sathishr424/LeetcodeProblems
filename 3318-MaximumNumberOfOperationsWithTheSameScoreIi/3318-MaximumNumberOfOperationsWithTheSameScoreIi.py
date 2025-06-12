# Last updated: 12/6/2025, 5:35:50 am
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) <= 3: return 1
        n = len(nums)
        @cache
        def rec(i, j, target):
            if i >= j: return 0
            
            left = nums[i] + nums[i+1]
            right = nums[j] + nums[j-1]
            mid = nums[i] + nums[j]
            ans = 0
            if left == target:
                ans = max(ans, rec(i+2, j, target) + 1)
            if right == target:
                ans = max(ans, rec(i, j-2, target) + 1)
            if mid == target:
                ans = max(ans, rec(i+1, j-1, target) + 1)
            return ans
        
        i = 0
        j = len(nums)-1
        return max(rec(i+1, j-1, nums[i] + nums[j]), rec(i+2, j, nums[i] + nums[i+1]), rec(i, j-2, nums[j] + nums[j-1])) + 1