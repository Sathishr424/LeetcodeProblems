# Last updated: 8/4/2025, 7:21:55 am
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = SortedList()
        n = len(nums)

        arr.add(nums[-1])
        ret = deque([])
        ret.appendleft(0)

        for i in range(n-2, -1, -1):
            index = bisect_right(arr, nums[i]-1)
            ret.appendleft(index)
            arr.add(nums[i])
        
        return list(ret)
