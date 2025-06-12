# Last updated: 12/6/2025, 5:39:25 am
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            nums[i] = (nums[nums[i]] % 1000) * 1000 + nums[i]

        for i in range(n):
            nums[i] = nums[i] // 1000
        
        return nums