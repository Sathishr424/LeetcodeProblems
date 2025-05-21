# Last updated: 22/5/2025, 3:00:36 am
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)

        prefixes = [0] * n
        s = 0
        for i in range(n-1, -1, -1):
            s += nums[i]
            prefixes[i] = s

        sl = SortedList()
        ret = 0

        for i in range(n):
            sl.add(prefixes[i])
            curr = prefixes[i] - nums[i]

            l = sl.bisect_left(curr+lower)
            r = sl.bisect_right(curr+upper)

            ret += r - l
        
        return ret
            

        