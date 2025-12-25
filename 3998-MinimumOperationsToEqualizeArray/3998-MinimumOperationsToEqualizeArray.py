# Last updated: 12/25/2025, 7:09:22 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for num in nums:
            if num != nums[0]: return 1

        return 0