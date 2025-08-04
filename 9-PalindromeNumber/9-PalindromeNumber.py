# Last updated: 4/8/2025, 2:31:07 pm
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        tot = n * (n + 1) // 2

        for num in nums:
            tot -= num
        
        return tot