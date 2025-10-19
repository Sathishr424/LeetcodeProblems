# Last updated: 19/10/2025, 1:37:35 pm
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums = set(nums)

        for num in range(k, 1000, k):
            if num not in nums: return num

        return -1