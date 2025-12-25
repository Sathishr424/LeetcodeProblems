# Last updated: 12/25/2025, 7:09:57 PM
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        ret = n-1

        for i in range(n):
            curr = ceil(nums[i] / k)

            index = bisect_left(nums, curr, hi=i)
            right = n - i - 1
            left = index
            ret = min(ret, right + left)

        return ret