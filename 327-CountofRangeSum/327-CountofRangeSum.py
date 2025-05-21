# Last updated: 22/5/2025, 2:56:04 am
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # [1, 2, 3, 4, -2, 4, 9, 0, -1] => 7, 9
        # [-2, 4, 9, 0, -1]
        n = len(nums)

        prefixes = [0] * n
        s = 0
        for i in range(n-1, -1, -1):
            s += nums[i]
            prefixes[i] = s
        # print(prefixes)

        prefix = 0
        sl = SortedList()
        ret = 0

        for i in range(n):
            sl.add(prefixes[i])
            curr = prefixes[i] - nums[i]

            l = sl.bisect_left(curr+lower)
            r = sl.bisect_right(curr+upper)

            ret += r - l
            # print(list(sl), nums[i], curr, (l, r), ret)
        
        return ret
            

        