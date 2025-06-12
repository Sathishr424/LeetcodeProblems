# Last updated: 12/6/2025, 5:36:25 am
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0: return 0
        n = len(nums)
        ret = float('inf')
        
        sl = SortedList()
        sl.add(nums[0])

        for i in range(x, n):
            index = sl.bisect_left(nums[i])
            if index < len(sl):
                ret = min(abs(nums[i] - sl[index]), ret)
            if index-1 >= 0:
                ret = min(abs(nums[i] - sl[index-1]), ret)
            
            sl.add(nums[i-x+1])
        
        return ret