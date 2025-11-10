# Last updated: 11/11/2025, 1:27:12 am
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        ans = 0
        sl = SortedList()
        sl.add(0)
        s = 0
        for i in range(n):
            s += nums[i]
            left = sl.bisect_left(s - upper)
            right = sl.bisect_right(s - lower)
            ans += right - left
            sl.add(s)
        
        return ans