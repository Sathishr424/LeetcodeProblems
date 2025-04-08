# Last updated: 8/4/2025, 6:39:12 am
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        last = max(nums) + 1

        arr = [0] * (last+1)

        for num in nums:
            arr[num] += 1
        
        for num in range(last):
            if arr[num] > 1:
                arr[num+1] += arr[num]-1
                res += arr[num]-1

        return res + arr[last] * (arr[last]-1) // 2

        

