# Last updated: 30/10/2025, 8:40:22 pm
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        n = len(nums)

        nums = set(nums)
        for bit in range(32):
            if (1 << bit) not in nums:
                return 1 << bit

        return 0