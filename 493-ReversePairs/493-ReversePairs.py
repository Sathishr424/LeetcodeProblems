# Last updated: 22/4/2025, 2:18:33 am
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        arr = SortedList()
        ret = 0

        for i, num in enumerate(nums):
            ret += i - arr.bisect_right(num*2)
            arr.add(num)
        
        return ret