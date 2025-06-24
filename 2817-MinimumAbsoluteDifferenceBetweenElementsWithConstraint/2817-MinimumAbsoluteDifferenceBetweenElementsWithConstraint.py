# Last updated: 24/6/2025, 2:32:48 pm
inf = float('inf')
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        n = len(nums)
        left = SortedList()
        ret = inf
        for i in range(x, n):
            left.add(nums[i - x])
            index = left.bisect_left(nums[i])

            if index < len(left):
                ret = min(ret, abs(nums[i] - left[index]))
            
            if index - 1 >= 0:
                ret = min(ret, abs(nums[i] - left[index - 1]))
            
        return ret