# Last updated: 12/25/2025, 7:07:58 PM
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        for i in range(n):
            index = bisect_right(nums, nums[i])
            rem = n - index
            if rem >= k: ans += 1

        return ans
            