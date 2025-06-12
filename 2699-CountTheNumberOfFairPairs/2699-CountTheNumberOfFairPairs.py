# Last updated: 12/6/2025, 5:37:11 am
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        ret = 0

        for num in nums:
            left = lower-num
            right = upper-num

            l = sl.bisect_left(left)
            r = sl.bisect_right(right)

            ret += r - l

            sl.add(num)
        
        return ret