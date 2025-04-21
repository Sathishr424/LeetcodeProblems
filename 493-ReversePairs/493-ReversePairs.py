# Last updated: 22/4/2025, 2:18:02 am
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = SortedList()
        ret = 0
        
        for i, num in enumerate(nums):
            ret += i - bisect_right(arr, num*2)
            arr.add(num)
        
        return ret