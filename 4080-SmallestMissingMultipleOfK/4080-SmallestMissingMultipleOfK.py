# Last updated: 12/25/2025, 7:08:25 PM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums = set(nums)

        for num in range(k, 1000, k):
            if num not in nums: return num

        return -1