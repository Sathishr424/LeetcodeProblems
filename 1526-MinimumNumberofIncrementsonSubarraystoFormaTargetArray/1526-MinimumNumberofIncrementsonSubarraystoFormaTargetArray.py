# Last updated: 30/10/2025, 6:58:50 pm
class Solution:
    def minNumberOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ans = nums[0]
        for i in range(1, n):
            ans += max(nums[i] - nums[i - 1], 0)
        
        return ans