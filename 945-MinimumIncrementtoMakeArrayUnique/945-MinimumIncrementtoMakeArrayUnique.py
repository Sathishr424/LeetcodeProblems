# Last updated: 8/4/2025, 6:38:11 am
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        last = max(nums)

        arr = [0] * (last+2)

        for num in nums:
            arr[num] += 1
        
        for num in range(last+1):
            if arr[num] > 1:
                arr[num+1] += arr[num]-1
                res += arr[num]-1
                arr[num] = 1
        # print(arr, arr[last+1])
        res += arr[last+1] * (arr[last+1]-1) // 2
        return res

        

