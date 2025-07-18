# Last updated: 18/7/2025, 2:33:21 pm
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def rec(x, y, z):
            if  y >= n or z >= n:
                curr = nums[x]
                if y < n: curr = max(curr, nums[y])
                if z < n: curr = max(curr, nums[z])
                return curr
            one = rec(z, z + 1, z + 2) + max(nums[x], nums[y])
            two = rec(y, z + 1, z + 2) + max(nums[x], nums[z])
            three = rec(x, z + 1, z + 2) + max(nums[y], nums[z])

            return min(one, two, three)
        
        ans = rec(0, 1, 2)
        rec.cache_clear()
        return ans