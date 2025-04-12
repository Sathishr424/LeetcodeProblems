# Last updated: 12/4/2025, 9:41:20 pm
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k