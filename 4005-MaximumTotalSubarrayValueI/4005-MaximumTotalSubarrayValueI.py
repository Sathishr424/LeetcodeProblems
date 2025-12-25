# Last updated: 12/25/2025, 7:09:18 PM
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        maxi = max(nums)
        mini = min(nums)

        ans = maxi - mini
        return ans * k