# Last updated: 13/7/2025, 12:58:50 am
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def rec(index):
            if index == n:
                return 0

            ans = 0
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    ans = max(ans, rec(i))
            
            return ans + 1
        
        return max([rec(i) for i in range(n)])