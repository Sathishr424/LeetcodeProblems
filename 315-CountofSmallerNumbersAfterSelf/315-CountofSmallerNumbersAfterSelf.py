# Last updated: 15/4/2025, 11:19:35 pm
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n

        freq = {}
        index = 0

        for num in sorted(nums):
            if num not in freq:
                freq[num] = index
                index += 1
        
        n = len(freq)
        arr = SortedList()

        for j in range(len(nums)-1, -1, -1):
            num = nums[j]
            i = freq[num]

            index = bisect_left(arr, i)
            arr.add(i)
            # print(arr, i, index)
            ret[j] = index
        
        return ret
        