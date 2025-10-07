# Last updated: 7/10/2025, 7:23:58 pm
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = n * (n + 1) // 2

        for num in nums:
            s -= num
        
        return s