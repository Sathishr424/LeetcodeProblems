# Last updated: 12/6/2025, 5:39:36 am
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (max(nums)+1)
        for num in nums: arr[num] += 1
        index = 0
        for i, a in enumerate(arr):
            for j in range(a):
                nums[index] = i
                index += 1
        
        return max([nums[i]+nums[n-(i+1)] for i in range(n//2)])
