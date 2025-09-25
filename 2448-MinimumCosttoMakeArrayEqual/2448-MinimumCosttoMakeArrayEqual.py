# Last updated: 26/9/2025, 12:32:24 am
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)

        def calc(num):
            c = 0
            for i in range(n):
                diff = abs(num - nums[i])
                c += diff * cost[i]
            return c

        l = min(nums)
        r = max(nums)

        while l < r:
            mid = (l + r) // 2

            if calc(mid) <= calc(mid + 1):
                r = mid
            else:
                l = mid + 1
        
        return calc(l)