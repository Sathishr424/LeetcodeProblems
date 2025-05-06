# Last updated: 6/5/2025, 1:19:30 pm
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [0] * n
        for i in range(n):
            ans[i] = nums[nums[i]]
        return ans