# Last updated: 26/4/2025, 8:58:44 am
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        
        """
        [1,3,5,2,7,5]
        [5,3,5,1,2,1,5,8,7,1,2,5,2]
        """

        prev = 0
        left = 0
        ret = 0
        arr = SortedList()

        for i, num in enumerate(nums):
            arr.add(num)

            if arr[0] < minK or arr[-1] > maxK:
                prev = 0
                arr.clear()
                left = i+1
                continue
            # print(arr, arr[0], arr[-1])
            while arr and arr[0] == minK and arr[-1] == maxK:
                arr.remove(nums[left])
                left += 1
                prev += 1
            
            ret += prev
        
        return ret