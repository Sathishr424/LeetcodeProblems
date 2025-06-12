# Last updated: 12/6/2025, 5:33:55 am
class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        l = 0
        r = n*n

        while l < r:
            mid = ceil((l+r) / 2)

            if mid*w > maxWeight:
                r = mid-1
            else:
                l = mid
        # 1 2 3 4 4 5 6
        return l