# Last updated: 8/4/2025, 7:41:19 am
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = SortedList()
        arr.add(nums[-1])
        ret = [0] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            index = bisect_right(arr, nums[i]-1)
            ret[i] = index
            arr.add(nums[i])
        
        return ret
