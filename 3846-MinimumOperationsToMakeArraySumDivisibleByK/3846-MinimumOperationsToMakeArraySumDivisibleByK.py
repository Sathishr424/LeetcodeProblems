# Last updated: 12/6/2025, 5:33:36 am
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k