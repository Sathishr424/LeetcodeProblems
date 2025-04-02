# Last updated: 2/4/2025, 11:26:48 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        arr = [-float('inf')] * n
        for i in range(n):
            for j in range(i+1, n):
                arr[j] = max(nums[i] - nums[j], arr[j])

        for i in range(n):
            for j in range(i+1, n):
                ret = max(arr[i] * nums[j], ret)
        
        return ret if ret > 0 else 0
