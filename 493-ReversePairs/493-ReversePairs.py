# Last updated: 22/4/2025, 1:23:47 am
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        arr = SortedList()
        arr.add(nums[-1] * 2)
        ret = 0
        for i in range(n-2, -1, -1):
            num = nums[i]

            index = bisect_left(arr, num)
            ret += index
            arr.add(num * 2)
        
        return ret