# Last updated: 12/6/2025, 5:35:45 am
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        
        return ans
