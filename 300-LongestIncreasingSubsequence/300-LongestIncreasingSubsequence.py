# Last updated: 15/4/2025, 5:27:49 pm
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def rec(index):
            ans = 0
            for i in range(index+1, n):
                if nums[i] > nums[index]: ans = max(ans, rec(i) + 1)
            
            return ans
        
        return max([rec(i) + 1 for i in range(n-1, -1, -1)])